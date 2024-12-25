from collections import deque


def load_obstacles(filename: str) -> list[tuple[int, int]]:
    obstacles = []
    with open(filename) as file:
        for i, line in enumerate(file):
            nums = line.strip().split(',')
            obstacles.append((int(nums[1]), int(nums[0])))
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

        # Reached exit
        if row == rows - 1 and col == cols - 1:
            return cost

        # Can't / Shouldn't move here
        if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in illegal or (row, col) in visited:
            continue

        visited.add((row, col))

        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            q.append((row + direction[0], col + direction[1]))
            costs.append(cost + 1)

    return -1


def part1(memory_dimensions: tuple[int, int], nr_bytes: int) -> int:
    obstacles = set(load_obstacles('input.txt')[:nr_bytes])
    return bfs(memory_dimensions[0], memory_dimensions[1], obstacles)


# TODO: This is the naive solution; At least implement a binary search one
def part2(memory_dimensions: tuple[int, int]) -> tuple[int, int]:
    all_obstacles = load_obstacles('input.txt', )
    cur_obstacles = set(all_obstacles)
    for byte_idx in range(len(all_obstacles) - 1, -1, -1):
        cur_obstacles.remove(all_obstacles[byte_idx])
        if bfs(memory_dimensions[0], memory_dimensions[1], cur_obstacles) != -1:
            return all_obstacles[byte_idx][1], all_obstacles[byte_idx][0]
    return -1, -1


print(part1((71, 71), 1024))
print(part2((71, 71)))
