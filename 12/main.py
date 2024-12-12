def load_field(file_name: str) -> list[list[str]]:
    field: list[list[str]] = []
    with open(file_name) as file:
        for line in file:
            field.append(list(line.strip()))
    return field


# Returns (nr_fences, area)
def traverse_region(field: list[list[str]], region_name: str, row: int, col: int, visited: list[list[bool]]) -> tuple[
    int, int]:
    if row < 0 or row >= len(field) or col < 0 or col >= len(field[0]) or field[row][col] != region_name:
        return 1, 0

    if visited[row][col]:
        return 0, 0

    visited[row][col] = True

    fences, area = 0, 1

    for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        res = traverse_region(field, region_name, row + direction[0], col + direction[1], visited)
        fences += res[0]
        area += res[1]

    return fences, area


def part1():
    field = load_field("input.txt")
    visited = [[False for _ in range(len(field[0]))] for _ in range(len(field))]
    cost = 0
    for row in range(len(field)):
        for col in range(len(field[0])):
            if visited[row][col]:
                continue
            fences, area = traverse_region(field, field[row][col], row, col, visited)
            cost += fences * area
    return cost


print(part1())
