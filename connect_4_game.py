from collections import deque
ROWS, COLS = 6, 7
CONNECT_RANGE = 4


def get_valid_column():
    print(f"Player {player}, please choose a column:")

    while True:
        try:
            val = int(input())
        except ValueError:
            print("Enter a valid value:")
            continue

        if not 0 <= val - 1 < COLS:
            print("Column out of range/ Enter new value: ")
            continue

        if len(list(filter(lambda x: (x == 0), [board[r][val - 1] for r in range(ROWS)]))) == 0:
            print("Slot full/Choose another slot: ")
            continue
        else:
            return val - 1


def set_slot(a, b):
    for row in range(ROWS - 1, -1, -1):
        if board[row][b] == 0:
            board[row][b] = a
            [print(" ".join([str(x) for x in board[row]])) for row in range(ROWS)]
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
            print(f"Player {player} won")
            loop = False
            break


board = [[0 for c in range(COLS)] for r in range(ROWS)]
[print(" ".join(str(0) for col in range(COLS))) for row in range(ROWS)]

players = deque([1, 2])

loop = True
while loop:
    player = players.popleft()
    column = get_valid_column()
    players.append(player)
    player_point = set_slot(player, column)
    check_for_connection(player_point[0], player_point[1])
