import functools
import operator
import regex


def load_robots_info(file_name: str) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    robots_info = []
    with open(file_name) as file:
        for line in file:
            pos_vel = list(map(int, regex.findall('-?\\d+', line)))
            pos = (pos_vel[0], pos_vel[1])
            vel = (pos_vel[2], pos_vel[3])
            robots_info.append((pos, vel))
    return robots_info


def pos_to_quadrant(width: int, height: int, x: int, y: int) -> int:
    w2 = width // 2
    h2 = height // 2
    # w_mid_margin = width % 2 == 1  # Needed to exclude the middle
    # h_mid_margin = height % 2 == 1
    if x < w2 and y < h2:
        return 0
    if x > w2 and y < h2:
        return 1
    if x < w2 and y > h2:
        return 2
    if x > w2 and y > h2:
        return 3
    return -1


def part1():
    time_s = 100
    width, height = 101, 103
    robots_info = load_robots_info('input.txt')
    robots_in_quadrant: list[int] = [0, 0, 0, 0]

    # Calculate positions after 100 seconds
    for robot_info in robots_info:
        pos, vel = robot_info
        x = (pos[0] + vel[0] * time_s) % width
        y = (pos[1] + vel[1] * time_s) % height
        # Get quadrant
        quadrant = pos_to_quadrant(width, height, x, y)
        if quadrant != -1:
            robots_in_quadrant[quadrant] += 1

    return functools.reduce(operator.mul, robots_in_quadrant, 1)


print(part1())
