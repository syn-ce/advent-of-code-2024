def board_bounds(board: list[list[chr]], row: int, col: int) -> bool:
    return not (row < 0 or row >= len(board) or col < 0 or col >= len(board[0]))


def circle_in_simulation(board: list[list[chr]], row: int, col: int, xdir: int, ydir: int,
                         visited: dict[(int, int), set[(int, int)]]):
    visited[(row, col)] = {(xdir, ydir)}

    # While guard is on board
    while board_bounds(board, row, col):
        for i in range(4):
            if not board_bounds(board, row + ydir, col + xdir) or board[row + ydir][col + xdir] != '#':
                break
            # Need to turn
            # 0, -1 -> 1, 0 -> 0, 1 -> -1, 0 -> 0, -1
            if xdir == 0 and ydir == -1:
                xdir, ydir = 1, 0
            elif xdir == 1 and ydir == 0:
                xdir, ydir = 0, 1
            elif xdir == 0 and ydir == 1:
                xdir, ydir = -1, 0
            else:
                xdir, ydir = 0, -1
        if not board_bounds(board, row + ydir, col + xdir):  # Left board
            return False
        if board[row + ydir][col + xdir] == '#':  # Still facing wall -> enclosed
            return True

        # March forward
        row += ydir
        col += xdir

        if (row, col) not in visited:
            visited[(row, col)] = set()
        if (xdir, ydir) in visited[(row, col)]:
            return True
        visited[(row, col)].add((xdir, ydir))

    return False


def load_board(file_name: str) -> (list[list[chr]], int, int):
    with open(file_name, 'r') as file:
        start_row = -1  # Careful, -1 is a valid index in python
        start_col = -1
        board: list[list[chr]] = []
        # Construct board and find starting position
        for i, line in enumerate(file):
            board.append(list(line.strip()))
            if start_row == -1:
                try:
                    idx = board[i].index('^')
                    start_row = i
                    start_col = idx
                except ValueError:
                    pass

        return board, start_row, start_col


board, start_row, start_col = load_board('input.txt')
# Simulate starting from (start_row, start_col)
visited: dict[(int, int), set[(int, int)]] = dict()

circle_count = 0
for row in range(len(board)):
    print(f'{round(row / len(board), 3) * 100}%')
    for col in range(len(board[0])):
        if board[row][col] == '.':
            board[row][col] = '#'
            visited.clear()
            if circle_in_simulation(board, start_row, start_col, 0, -1, visited):
                circle_count += 1
            board[row][col] = '.'

print(circle_count)
