def dfs(board: list[list[chr]], row: int, col: int, word: str, idx: int, xdir: int, ydir: int):
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[row]) or board[row][col] != word[idx]:
        return 0

    if idx == len(word) - 1:
        return 1

    if not (xdir == 0 and ydir == 0):  # Only check one direction
        return dfs(board, row + xdir, col + ydir, word, idx + 1, xdir, ydir)

    res = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            res += dfs(board, row + i, col + j, word, idx + 1, i, j)

    return res


with open('input.txt', 'r') as file:
    board = []
    for line in file:
        board.append(list(line.strip()))

    appearances = 0
    # Dfs on board
    for row in range(len(board)):
        for col in range(len(board[row])):
            appearances += dfs(board, row, col, "XMAS", 0, 0, 0)

    print(appearances)
