def simulate(board: list[list[int]], row: int, col: int, xdir: int, ydir: int, visited: set[(int, int)]):
    visited.add((row, col))
    # While guard is on board
    while 0 <= row + ydir < len(board) and 0 <= col + xdir < len(board[0]):
        while board[row + ydir][col + xdir] == '#':
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

        # March forward
        row += ydir
        col += xdir

        visited.add((row, col))


with open("input.txt", 'r') as file:
    start_row = -1  # Careful, -1 is a valid index in python
    start_col = -1
    board: list[list[chr]] = []
    # Construct board and find starting position
    for i, line in enumerate(file):
        board.append(list(line.strip()))
        print(board[i])
        if start_row == -1:
            try:
                idx = board[i].index('^')
                start_row = i
                start_col = idx
            except ValueError:
                pass

    # Simulate starting from (start_row, start_col)
    visited: set[(int, int)] = set()
    simulate(board, start_row, start_col, 0, -1, visited)
    print(len(visited))
