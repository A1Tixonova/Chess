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


def write_turn(a: str, b: str, name: str) -> bool:
    a1, a2 = to_tuple(a)
    b1, b2 = to_tuple(b)
    if (a1 < 0) or (a1 > 7) or (a2 < 0) or (a2 > 7) or (b1 < 0) or (b1 > 7) or (b2 < 0) or (b2 > 7):
        raise Exception('Wrong coordinates')
    with open(name, "r") as read_file:
        cur_board: dict = json.load(read_file)
        if a not in cur_board:
            raise Exception("Wrong coordinates")
        if check_turn(cur_board, a, b) == 1:
            temp = cur_board.pop(a)
            cur_board[b] = temp

    with open(name, 'w') as file:
        json.dump(cur_board, file)


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


def check_checkmate(board: dict, color: str):
    pos = 0
    for i, j in board.items():
        if j == ('k' + color):
            pos = i
    x, y = to_tuple(pos)
    t = []


def get_king_turns(x: int, y: int):
    t = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x + 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]
    while True:
        ind = -1
        for i, x0, y0 in enumerate(t):
            if x0 > 7 or x0 < 0 or y0 < 0 or y0 > 7:
                ind = i
                break
        if ind == -1:
            break
        else:
            t.pop(ind)


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

    if fig == 'bb' or fig == 'bw' or fig == 'qw' or fig == 'qb':
        if y == 0 and all(map(lambda t: from_tuple((t, a2)) not in board, range(min(a1, b1) + 1, max(a1, b1)))):
            return 1
        if x == 0 and all(map(lambda t: from_tuple((a1, t)) not in board, range(min(a2, b2) + 1, max(a2, b2)))):
            return 1

    if fig == 'bb' or fig == 'bw' or fig == 'qw' or fig == 'qb':
        if x == y and x > 0 and map(lambda t: from_tuple((a1 + t, a2 + t)) not in board, range(1, x)):
            return 1
        if x == y and x < 0 and map(lambda t: from_tuple((a1 - t, a2 - t)) not in board, range(1, -x)):
            return 1
        if x == -y and x > 0 and map(lambda t: from_tuple((a1 + t, a2 - t)) not in board, range(1, x)):
            return 1
        if x == -y and x < 0 and map(lambda t: from_tuple((a1 - t, a2 + t)) not in board, range(1, -x)):
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
                return 3

    if fig == 'kb':
        if abs(x) == 2 and y == 0 and a2 == 7:
            a1, b1 = min(a1, b1), max(a1, b1)
            if (from_tuple((7, a1 + 1)) not in board) and (from_tuple((7, a1 + 2)) not in board):
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


bo = 'firstboard.json'
create_board(bo)
print_board(bo)
write_turn('b1', 'c3', bo)
print_board(bo)
