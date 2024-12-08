def load_board(file_name: str) -> tuple[list[list[str]], int, int]:
    start_row = -1  # Careful, -1 is a valid index in python
    start_col = -1
    board: list[list[str]] = []

    with open(file_name, 'r') as file:
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


def board_bounds(board: list[list[str]], row: int, col: int) -> bool:
    return not (row < 0 or row >= len(board) or col < 0 or col >= len(board[0]))


def simulate_detect_cycle(board: list[list[str]], row: int, col: int, xdir: int, ydir: int,
                          visited: dict[tuple[int, int], set[tuple[int, int]]]):
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


def part1():
    board, start_row, start_col = load_board('input.txt')

    # Simulate starting from (start_row, start_col)
    visited: dict[tuple[int, int], set[tuple[int, int]]] = dict()
    simulate_detect_cycle(board, start_row, start_col, 0, -1, visited)

    return len(visited)


def part2():
    board, start_row, start_col = load_board('input.txt')

    # Simulate starting from (start_row, start_col) -> get visited cells
    visited: dict[tuple[int, int], set[tuple[int, int]]] = dict()
    simulate_detect_cycle(board, start_row, start_col, 0, -1, visited)

    circles = 0
    del visited[(start_row, start_col)]  # Can't place obstacle at initial guard position
    # Only obstacles placed at positions in `visited` will be reachable
    for i, pos in enumerate(visited):
        row, col = pos
        if i % (len(visited) // 100) == 0:  # Printing progress
            # Works in terminal, doesn't display in PyCharm (flushing doesn't fix that)
            print(f'{round(i * 100 / len(visited), 2):.2f}%', end='\r')
        if board[row][col] == '.':
            board[row][col] = '#'
            if simulate_detect_cycle(board, start_row, start_col, 0, -1, dict()):
                circles += 1
            board[row][col] = '.'

    print('\033[K', end='\r')  # Erase (potentially printed) progress
    return circles


print(part1())
print(part2())
