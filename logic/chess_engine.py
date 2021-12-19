import json


def create_board(name: str) -> None:
    data = {
        'a1': 'rw', 'a2': 'pw',
        'b1': 'nw', 'b2': 'pw',
        'c1': 'bw', 'c2': 'pw',
        'd1': 'qw', 'd2': 'pw',
        'e1': 'kw', 'e2': 'pw',
        'f1': 'bw', 'f2': 'pw',
        'g1': 'nw', 'g2': 'pw',
        'h1': 'rw', 'h2': 'pw',

        'a8': 'rb', 'a7': 'pb',
        'b8': 'nb', 'b7': 'pb',
        'c8': 'bb', 'c7': 'pb',
        'd8': 'qb', 'd7': 'pb',
        'e8': 'kb', 'e7': 'pb',
        'f8': 'bb', 'f7': 'pb',
        'g8': 'nb', 'g7': 'pb',
        'h8': 'rb', 'h7': 'pb',
    }
    with open(name, 'w') as file:
        json.dump(data, file)


def write_turn(a: str, b: str, name: str, tcol) -> bool:
    a1, a2 = to_tuple(a)
    b1, b2 = to_tuple(b)
    x = b1 - a1
    y = b2 - a2
    if (a1 < 0) or (a1 > 7) or (a2 < 0) or (a2 > 7) or (b1 < 0) or (b1 > 7) or (b2 < 0) or (b2 > 7):
        raise Exception('Wrong coordinates')
    with open(name, "r") as read_file:
        cur_board: dict = json.load(read_file)
        if a not in cur_board:
            return False

        turn = check_turn(cur_board, a, b)
        color = cur_board[a][1]
        if tcol != color:
            return False
        if cur_board[a][0] == 'k' and turn!=3:
            l = list(filter(lambda x: not check_checkmate(cur_board, x, color), get_king_turns(a1, a2)))
            if b in l:
                temp = cur_board.pop(a)
                cur_board[b] = temp
        else:
            kp = king_pos(cur_board, color)
            if check_checkmate(cur_board, kp, color):
                temp = cur_board.pop(a)
                cur_board[b] = temp
                if check_checkmate(cur_board, kp, color):
                    return False
            else:

                if turn == 1:
                    temp = cur_board.pop(a)
                    cur_board[b] = temp
                elif turn == 2:
                    ind = from_tuple((a1 + x, a2))
                    en = cur_board[ind]
                    if en[0] == cur_board[a][0] and en[1] != cur_board[a][1]:
                        temp = cur_board.pop(a)
                        cur_board.pop(ind)
                        cur_board[b] = temp
                elif turn == 3:
                    if cur_board[a][1]=='w':
                        if x>0:
                            a1 = 'h1'
                            a2 = 'f1'
                        else:
                            a1 = 'a1'
                            a2 = 'd1'
                    else:
                        if x>0:
                            a1 = 'h8'
                            a2 = 'f8'
                        else:
                            a1 = 'a8'
                            a2 = 'd8'
                    temp = cur_board.pop(a1)
                    cur_board[a2] = temp
                    temp = cur_board.pop(a)
                    cur_board[b] = temp
                    kp = king_pos(cur_board, color)
                    if check_checkmate(cur_board, b, color):
                        return False
                else:
                    return False

    with open(name, 'w') as file:
        json.dump(cur_board, file)
    return True


def print_board(name: str) -> None:
    with open(name, "r") as read_file:
        cur_board: dict = json.load(read_file)
        for i in range(8):
            for j in range(8):
                t = from_tuple((j, 7 - i))
                if t in cur_board:
                    print(cur_board[t], end=' ')
                else:
                    print('**', end=' ')
            print()
        print()

# console.log('sdgf');

def king_pos(board: dict, color: str) -> tuple:
    pos = 0
    col = 'k' + color
    for i, j in board.items():
        if j == col:
            pos = i
    return pos


def check_checkmate(board: dict, pos, col) -> bool:
    for i, j in board.items():
        if j[1] != col and check_turn(board, i, pos):
            return True

    return False


def get_king_turns(x: int, y: int) -> list:
    t = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x + 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]
    while True:
        ind = -1
        for i, x in enumerate(t):
            if x[0] > 7 or x[0] < 0 or x[1] < 0 or x[1] > 7:
                ind = i
                break
        if ind == -1:
            break
        else:
            t.pop(ind)
    return list(map(lambda x: from_tuple(x), t))


def check_turn(board: dict, a: str, b: str) -> int:
    a1, a2 = to_tuple(a)
    b1, b2 = to_tuple(b)
    x = b1 - a1
    y = b2 - a2
    fig = board[a]
    if b in board and board[b][1] == fig[1]:
        return 0

    if fig == 'pw':
        if y == 1 and x == 0 and (b not in board):
            return 1
        if y == 2 and x == 0 and a2 == 1 and (b not in board):
            return 1
        if y == 1 and (x == -1 or x == 1) and (b in board) and board[b][1] == 'b':
            return 1
        if y == 1 and (x == 1 or x == -1) and board[from_tuple((b1, b2 - 1))] == 'pb':
            return 2

    if fig == 'pb':
        if y == -1 and x == 0 and (b not in board):
            return 1
        if y == -2 and x == 0 and a2 == 6 and (b not in board):
            return 1
        if y == -1 and (x == -1 or x == 1) and (b in board) and board[b][1] == 'w':
            return 1
        if y == -1 and (x == 1 or x == -1) and board[from_tuple((b1, b2 + 1))] == 'pw':
            return 2

    if fig == 'rb' or fig == 'rw' or fig == 'qw' or fig == 'qb':
        if y == 0 and all(map(lambda t: from_tuple((t, a2)) not in board, range(min(a1, b1) + 1, max(a1, b1)))):
            return 1
        if x == 0 and all(map(lambda t: from_tuple((a1, t)) not in board, range(min(a2, b2) + 1, max(a2, b2)))):
            return 1

    if fig == 'bb' or fig == 'bw' or fig == 'qw' or fig == 'qb':
        if x == y and x > 0 and all(map(lambda t: from_tuple((a1 + t, a2 + t)) not in board, range(1, x))):
            return 1
        if x == y and x < 0 and all(map(lambda t: from_tuple((a1 - t, a2 - t)) not in board, range(1, -x))):
            return 1
        if x == -y and x > 0 and all(map(lambda t: from_tuple((a1 + t, a2 - t)) not in board, range(1, x))):
            return 1
        if x == -y and x < 0 and all(map(lambda t: from_tuple((a1 - t, a2 + t)) not in board, range(1, -x))):
            return 1

    if fig == 'nb' or fig == 'nw':
        if (abs(x) == 2 and abs(y) == 1) or (abs(x) == 1 and abs(y) == 2):
            return 1

    if fig == 'kw' or fig == 'kb':
        if abs(x) <= 1 and abs(y) <= 1:
            return 1

    if fig == 'kw':
        if abs(x) == 2 and y == 0 and a2 == 0:
            a1, b1 = min(a1, b1), max(a1, b1)
            if (from_tuple((0, a1 + 1)) not in board) and (from_tuple((0, a1 + 2)) not in board):
                if (x>0 and 'h1' in board and board['h1'] == 'rw') or (x<0 and 'a1' in board and board['a1'] == 'rw'):
                    return 3

    if fig == 'kb':
        if abs(x) == 2 and y == 0 and a2 == 7:
            a1, b1 = min(a1, b1), max(a1, b1)
            if (from_tuple((7, a1 + 1)) not in board) and (from_tuple((7, a1 + 2)) not in board):
                if (x>0 and 'h8' in board and board['h8'] == 'rb') or (x<0 and 'a8' in board and board['a8'] == 'rb'):
                    return 3

    return 0


def to_tuple(pos: str) -> tuple:
    if len(pos) != 2:
        raise Exception("The length of 'turn' string != 2")
    x, y = pos
    return ord(x) - 97, int(y) - 1


def from_tuple(pos: tuple) -> str:
    x, y = pos
    return chr(x + 97) + str(y + 1)


def debug(inp: list) -> None:
    bo = 'firstboard.json'
    create_board(bo)
    p = 'w'
    while inp:
        t = inp.pop(0).split()
        print(f'{p} turn')
        if write_turn(*t, bo, p):
            p = 'w' if p!='w' else 'b'

        print_board(bo)


if __name__ == '__main__':
    vz1 = ['b1 c3', 'd7 d5', 'c3 b1', 'd5 d4','e2 e4', 'd4 e3']
    vz2 = ['b1 c3', 'd7 d5', 'c3 b1', 'd5 d4','e2 e4', 'd4 e3']
    debug(vz2)
