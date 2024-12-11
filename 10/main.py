def read_map(file_name) -> list[list[int]]:
    board = []
    with open(file_name) as file:
        for line in file:
            board.append(list(map(int, line.strip())))
    return board


def one_step_up(board: list[list[int]], row: int, col: int, prev_value: int) -> bool:
    return 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == prev_value + 1


def count_reachable_nines(board: list[list[int]], row: int, col: int, visited: set[tuple[int, int]]) -> int:
    if (row, col) in visited:
        return 0

    visited.add((row, col))

    if board[row][col] == 9:
        return 1

    # Check neighbors
    nines = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for direction in directions:
        if one_step_up(board, row + direction[0], col + direction[1], board[row][col]):
            nines += count_reachable_nines(board, row + direction[0], col + direction[1], visited)

    return nines


def nr_of_ways_to_nines(board: list[list[int]], row: int, col: int, visited: set[tuple[int, int]]) -> int:
    if (row, col) in visited:
        return 0

    visited.add((row, col))

    if board[row][col] == 9:
        visited.remove((row, col))
        return 1

    # Check neighbors
    nines = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for direction in directions:
        if one_step_up(board, row + direction[0], col + direction[1], board[row][col]):
            nines += nr_of_ways_to_nines(board, row + direction[0], col + direction[1], visited)

    visited.remove((row, col))

    return nines


def part1():
    board = read_map('input.txt')
    rows, cols = len(board), len(board[0])

    trailhead_score = 0
    for row in range(rows):
        for col in range(cols):
            if board[row][col] != 0:
                continue
            trailhead_score += count_reachable_nines(board, row, col, set())
    return trailhead_score


def part2():
    board = read_map('input.txt')
    rows, cols = len(board), len(board[0])

    trailhead_score = 0
    for row in range(rows):
        for col in range(cols):
            if board[row][col] != 0:
                continue
            trailhead_score += nr_of_ways_to_nines(board, row, col, set())
    return trailhead_score


print(part1())
print(part2())
