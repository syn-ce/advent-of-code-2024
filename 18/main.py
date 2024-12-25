from collections import deque


def load_obstacles(filename: str, nr_bytes: int) -> set[tuple[int, int]]:
    obstacles = set()
    with open(filename) as file:
        for i, line in enumerate(file):
            if i == nr_bytes:
                break
            nums = line.strip().split(',')
            obstacles.add((int(nums[1]), int(nums[0])))
    return obstacles


def print_memory(rows: int, cols: int, illegal: set[tuple[int, int]]):
    for row in range(rows):
        row_out = []
        for col in range(cols):
            if (row, col) in illegal:
                row_out.append('#')
            else:
                row_out.append('.')
        print(''.join(row_out))


def bfs(rows: int, cols: int, illegal: set[tuple[int, int]]) -> int:
    q = deque([(0, 0)])
    costs = deque([0])
    visited = set()

    while len(q) > 0:
        row, col = q.popleft()
        cost = costs.popleft()

        print(row, col)

        # Reached exit
        if row == rows - 1 and col == cols - 1:
            return cost

        # Can't / Shouldn't move here
        if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in illegal or (row, col) in visited:
            print(f'Cannot do {row, col}')
            continue

        visited.add((row, col))

        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            q.append((row + direction[0], col + direction[1]))
            costs.append(cost + 1)

    return -1


def part1(memory_dimensions: tuple[int, int], nr_bytes: int) -> int:
    obstacles = load_obstacles('input.txt', nr_bytes)
    print_memory(memory_dimensions[0], memory_dimensions[1], obstacles)
    return bfs(memory_dimensions[0], memory_dimensions[1], obstacles)


print(part1((71, 71), 1024))
