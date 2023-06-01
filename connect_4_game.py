from collections import deque
ROWS = 6
COLS = 7
CONNECT_RANGE = 4


def get_valid_column():
    while True:
        try:
            val = int(input())
        except ValueError:
            print("Enter a valid value:")
            continue

        if not 0 <= val - 1 < COLS:
            print("Column out of range/ Enter new value: ")
            continue

        if len(list(filter(lambda x: (x == 0), [game_matrix[r][val - 1] for r in range(ROWS)]))) == 0:
            print("Slot full/Choose another slot: ")
            continue
        else:
            return val - 1


def check_4_connection(r, c):
    rows_range = (max(r - CONNECT_RANGE, 0), min(r + CONNECT_RANGE, ROWS))
    cols_range = (max(c - CONNECT_RANGE, 0), min(c + CONNECT_RANGE, COLS))

    second_diagonal = [game_matrix[a][b] for a in range(rows_range[0], rows_range[1])
                       for b in range(cols_range[0], cols_range[1]) if a + b == r + c]

    first_diagonal = [game_matrix[a][b] for a in range(rows_range[0], rows_range[1])
                      for b in range(cols_range[0], cols_range[1]) if a - b == r - c]

    vertical = [game_matrix[a][c] for a in range(rows_range[0], rows_range[1])]

    horizontal = [game_matrix[r][b] for b in range(cols_range[0], cols_range[1])]

    lists = deque([second_diagonal] + [first_diagonal] + [vertical] + [horizontal])

    while lists:
        current_line = "".join(str(x) for x in lists.popleft())
        if CONNECT_RANGE * str(player) in current_line:
            return True

    return False


game_matrix = [[0 for c in range(COLS)] for r in range(ROWS)]
[print(" ".join(str(0) for col in range(COLS))) for row in range(ROWS)]

players = deque([1, 2])

while True:
    player = players.popleft()
    player_point = [0, 0]
    print(f"Player {player}, please choose a column:")
    column = get_valid_column()
    players.append(player)

    for row in range(ROWS - 1, -1, -1):
        slot = game_matrix[row][column]

        if slot == 0:
            game_matrix[row][column] = player
            player_point = [row, column]
            break

    [print(" ".join([str(x) for x in game_matrix[row]])) for row in range(ROWS)]

    if check_4_connection(player_point[0], player_point[1]):
        print(f"Player {player} won")
        break
