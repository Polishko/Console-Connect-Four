from collections import deque
from colorama import Fore

ROWS, COLS = 6, 7
CONNECT_RANGE = 4


def get_valid_column():
    print(Fore.BLUE + f"Player {player}, please choose a column:" + Fore.RESET)

    while True:
        try:
            val = int(input())
        except ValueError:
            print(Fore.RED + f"Enter a valid value:" + Fore.RESET)
            continue

        if not 0 <= val - 1 < COLS:
            print(Fore.RED + f"Column out of range/ Enter new value: " + Fore.RESET)
            continue

        if len(list(filter(lambda x: (x == 0), [board[r][val - 1] for r in range(ROWS)]))) == 0:
            print(Fore.RED + "Slot full/Choose another slot: " + Fore.RESET)
            continue
        else:
            return val - 1


def print_board(a):
    [print(*row, sep=" ") for row in board]


def set_slot(a, b):
    for row in range(ROWS - 1, -1, -1):
        if board[row][b] == 0:
            board[row][b] = a
            print_board(board)
            return [row, b]


def check_for_connection(r, c):
    global loop
    low_r, high_r = max(r - CONNECT_RANGE, 0), min(r + CONNECT_RANGE, ROWS)
    low_c, high_c = max(c - CONNECT_RANGE, 0), min(c + CONNECT_RANGE, COLS)

    second_diagonal = [board[a][b] for a in range(low_r, high_r) for b in range(low_c, high_c) if a + b == r + c]
    first_diagonal = [board[a][b] for a in range(low_r, high_r) for b in range(low_c, high_c) if a - b == r - c]
    vertical = [board[a][c] for a in range(low_r, high_r)]
    horizontal = [board[r][b] for b in range(low_c, high_c)]

    lists = deque([second_diagonal] + [first_diagonal] + [vertical] + [horizontal])

    while lists:
        current_line = "".join(str(x) for x in lists.popleft())
        if CONNECT_RANGE * str(player) in current_line:
            print(Fore.GREEN + f"Player {player} won" + Fore.RESET)
            loop = False
            break


def check_if_draw(a):
    global loop
    if all([item != 0 for r in a for item in r]):
        print(Fore.BLUE + f"It's a draw!" + Fore.RESET)
        loop = False


board = [[0 for c in range(COLS)] for r in range(ROWS)]
print_board(board)

players = deque([1, 2])

loop = True
while loop:
    player = players.popleft()
    column = get_valid_column()
    players.append(player)
    player_point = set_slot(player, column)
    check_for_connection(player_point[0], player_point[1])
    check_if_draw(board)
