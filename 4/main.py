# Idea is to store the positions of 'middle cells' of the X formed by 'MAS' (i.e., the positions of the 'A')
# in one of two sets, depending on the direction of the 'MAS' (top left to bottom right, or bottom left to top right).
# Then we can simply take the length of their intersection
def dfs(board: list[list[chr]], row: int, col: int, word: str, idx: int, xdir: int, ydir: int,
        tlbr_diag: set[(int, int)], bltr_diag: set[(int, int)]):
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[row]) or board[row][col] != word[idx]:
        return

    if idx == len(word) - 1:
        if xdir == 1 and ydir == 1 or xdir == -1 and ydir == -1:
            tlbr_diag.add((row - xdir, col - ydir))  # Only works because 'MAS' is 3-letter word -> we have to go 1 back
        else:
            bltr_diag.add((row - xdir, col - ydir))
        return

    if not (xdir == 0 and ydir == 0):  # Only check one direction
        dfs(board, row + xdir, col + ydir, word, idx + 1, xdir, ydir, tlbr_diag, bltr_diag)
        return

    for i in [-1, 1]:  # Check diagonals
        for j in [-1, 1]:
            if i == 0 and j == 0:
                continue
            dfs(board, row + i, col + j, word, idx + 1, i, j, tlbr_diag, bltr_diag)


with open('input.txt', 'r') as file:
    board = []
    for line in file:
        board.append(list(line.strip()))

    appearances = 0
    tlbr_diag: set[(int, int)] = set()
    bltr_diag: set[(int, int)] = set()
    # Dfs on board
    for row in range(len(board)):
        for col in range(len(board[row])):
            dfs(board, row, col, "MAS", 0, 0, 0, tlbr_diag, bltr_diag)

    print(len(tlbr_diag.intersection(bltr_diag)))
