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


def check_turn(board: dict, a: tuple, b: tuple):
    return True


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
