from collections import deque


# Returns racetrack, start_pos
def load_racetrack(filename: str) -> tuple[list[list[str]], tuple[int, int]]:
    racetrack = []
    start_pos = (-1, -1)
    with open(filename) as file:
        for row, line in enumerate(file):
            racetrack.append([])
            for col, char in enumerate(line.strip()):
                if char == 'S':
                    start_pos = (row, col)
                racetrack[-1].append(char)

    return racetrack, start_pos


def assign_costs_to_track(racetrack: list[list[str]], start_pos: tuple[int, int]) -> dict[tuple[int, int], int]:
    q = deque([start_pos])
    costs = deque([0])
    track_costs = dict()

    while len(q) > 0:
        row, col = q.popleft()
        cost = costs.popleft()

        if row < 0 or row >= len(racetrack) or col < 0 or col >= len(racetrack[row]) or racetrack[row][col] == '#' or (
                row, col) in track_costs:  # Can't process or already processed
            continue

        track_costs[(row, col)] = cost

        for direction in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            q.append((row + direction[0], col + direction[1]))
            costs.append(cost + 1)

    return track_costs


def part1():
    racetrack, start_pos = load_racetrack('input.txt')
    track_costs = assign_costs_to_track(racetrack, start_pos)

    ways_to_cheat = 0
    # Go through all positions we drive through, try to cheat
    for pos, cost in track_costs.items():
        row, col = pos
        # Try to cheat in every direction
        for direction in [(0, 2), (2, 0), (0, -2), (-2, 0)]:
            new_pos = row + direction[0], col + direction[1]
            if new_pos in track_costs and track_costs[new_pos] - cost - 2 >= 100:
                ways_to_cheat += 1

    return ways_to_cheat


# TODO: think about improving this, there's probably a better solution
def part2():
    racetrack, start_pos = load_racetrack('input.txt')
    track_costs = assign_costs_to_track(racetrack, start_pos)

    ways_to_cheat = 0
    # Go through all positions we drive through, try to cheat
    for pos, cost in track_costs.items():
        # Try to cheat to every other path
        for new_pos in track_costs.keys():
            distance = abs(new_pos[0] - pos[0]) + abs(new_pos[1] - pos[1])
            if distance <= 20 and track_costs[new_pos] - cost - distance >= 100:
                ways_to_cheat += 1

    return ways_to_cheat


print(part1())
print(part2())
