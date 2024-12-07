# Idea is to store the positions of 'middle cells' of the X formed by 'MAS' (i.e., the positions of the 'A')
# in one of two sets, depending on the direction of the 'MAS' (top left to bottom right, or bottom left to top right).
# Then we can simply take the length of their intersection
def dfs(board: list[list[chr]], row: int, col: int, word: str, idx: int, xdir: int, ydir: int,
        xmas_positions: set[(int, int)]) -> int:
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[row]) or board[row][col] != word[idx]:
        return 0

    if idx == len(word) - 1:
        # Only works because 'MAS' is 3-letter word -> we have to go 1 back
        middle_pos = (row - xdir, col - ydir)
        if middle_pos in xmas_positions:  # Found second 'MAS' for this position -> must form cross
            return 1
        xmas_positions.add(middle_pos)
        return 0

    if not (xdir == 0 and ydir == 0):  # Only check one direction
        return dfs(board, row + xdir, col + ydir, word, idx + 1, xdir, ydir, xmas_positions)

    cross_count = 0
    for i in [-1, 1]:  # Check diagonals
        for j in [-1, 1]:
            if i == 0 and j == 0:
                continue
            cross_count += dfs(board, row + i, col + j, word, idx + 1, i, j, xmas_positions)
    return cross_count


with open('input.txt', 'r') as file:
    board = []
    for line in file:
        board.append(list(line.strip()))

    cross_count = 0
    xmas_positions = set()
    # Dfs on board
    for row in range(len(board)):
        for col in range(len(board[row])):
            cross_count += dfs(board, row, col, 'MAS', 0, 0, 0, xmas_positions)

    print(cross_count)
