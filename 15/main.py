def symbol_to_movement(symbol: str) -> tuple[int, int]:
    if symbol == '<':
        return 0, -1
    if symbol == '>':
        return 0, 1
    if symbol == '^':
        return -1, 0
    if symbol == 'v':
        return 1, 0


# Returns the warehouse, the movements (row, col), the starting pos of the robot (row, col)
def load_warehouse(filename: str) -> tuple[list[list[str]], list[tuple[int, int]], tuple[int, int]]:
    warehouse: list[list[str]] = []
    moves: list[tuple[int, int]] = []
    robot_pos: tuple[int, int] = (-1, -1)

    with open(filename) as file:
        parsing_moves = False
        for row, line in enumerate(file):
            if len(line.strip()) == 0:
                parsing_moves = True
                continue

            if not parsing_moves:
                warehouse_row: list[str] = []
                for col, char in enumerate(line.strip()):
                    if char == '@':
                        robot_pos = (row, col)
                        char = '.'
                    warehouse_row.append(char)
                warehouse.append(warehouse_row)
                continue

            moves.extend(map(symbol_to_movement, line.strip()))

    return warehouse, moves, robot_pos


def in_range(warehouse: list[list[str]], row: int, col: int) -> bool:
    return 0 <= row < len(warehouse) and 0 <= col < len(warehouse[row])


def try_move_in_direction(warehouse: list[list[str]], row: int, col: int, direction: tuple[int, int]) -> tuple[
    int, int]:
    new_row, new_col = row + direction[0], col + direction[1]
    if warehouse[new_row][new_col] == '.':  # Can move
        return new_row, new_col
    # Obstacle
    if warehouse[new_row][new_col] == '#':  # Wall -> can't move
        return row, col
    # Box -> try to push
    # Try to find empty space
    cur_row, cur_col = new_row, new_col

    while warehouse[cur_row][cur_col] == 'O':
        cur_row += direction[0]
        cur_col += direction[1]

    if warehouse[cur_row][cur_col] == '#':  # Can't push boxes
        return row, col

    # Found empty space -> Move boxes (Moving the first box into last position "moves every box"
    # if we ignore the identities of the boxes
    warehouse[cur_row][cur_col] = 'O'
    warehouse[new_row][new_col] = '.'
    return new_row, new_col


def part1():
    warehouse, moves, robot_pos = load_warehouse('input.txt')

    for move in moves:
        robot_pos = try_move_in_direction(warehouse, robot_pos[0], robot_pos[1], move)

    gps_sum = 0
    for row in range(len(warehouse)):
        for col in range(len(warehouse[row])):
            if warehouse[row][col] != 'O':
                continue
            gps_sum += 100 * row + col

    return gps_sum


print(part1())
