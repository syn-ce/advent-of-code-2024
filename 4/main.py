def read_board(file_name: str) -> list[list[str]]:
    with open(file_name, 'r') as file:
        board = []
        for line in file:
            board.append(list(line.strip()))
        return board


def count_appearances(board: list[list[str]], row: int, col: int, word: str, idx: int, xdir: int, ydir: int):
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[row]) or board[row][col] != word[idx]:
        return 0

    if idx == len(word) - 1:
        return 1

    if not (xdir == 0 and ydir == 0):  # Only check one direction
        return count_appearances(board, row + xdir, col + ydir, word, idx + 1, xdir, ydir)

    appearances = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            appearances += count_appearances(board, row + i, col + j, word, idx + 1, i, j)

    return appearances


def part1():
    board = read_board('input.txt')

    appearances = 0
    # Dfs on board
    for row in range(len(board)):
        for col in range(len(board[row])):
            appearances += count_appearances(board, row, col, "XMAS", 0, 0, 0)

    return appearances


# Idea is to store the positions of 'middle cells' of the X formed by 'MAS' (i.e., the positions of the 'A')
# in one of two sets, depending on the direction of the 'MAS' (top left to bottom right, or bottom left to top right).
# Then we can simply take the length of their intersection
def count_crosses(board: list[list[str]], row: int, col: int, word: str, idx: int, xdir: int, ydir: int,
                  xmas_positions: set[(int, int)]) -> int:
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[row]) or board[row][col] != word[idx]:
        return 0

    if idx == len(word) - 1:
        # Store cross at middle letter of the word
        # For 'MAS' (a 3-letter word), we will look 1=3//2 letter back from the end (i.e., look at 'A')
        middle_pos = (row - xdir * (len(word) // 2), col - ydir * (len(word) // 2))
        if middle_pos in xmas_positions:  # Found second 'MAS' for this position -> must form cross
            return 1
        xmas_positions.add(middle_pos)
        return 0

    if not (xdir == 0 and ydir == 0):  # Only check one direction
        return count_crosses(board, row + xdir, col + ydir, word, idx + 1, xdir, ydir, xmas_positions)

    crosses = 0
    for i in [-1, 1]:  # Check diagonals
        for j in [-1, 1]:
            if i == 0 and j == 0:
                continue
            crosses += count_crosses(board, row + i, col + j, word, idx + 1, i, j, xmas_positions)
    return crosses


def part2():
    board = read_board('input.txt')
    crosses = 0
    xmas_positions = set()
    # Dfs on board
    for row in range(len(board)):
        for col in range(len(board[row])):
            crosses += count_crosses(board, row, col, 'MAS', 0, 0, 0, xmas_positions)

    return crosses


print(part1())
print(part2())
