import functools
import heapq
import operator
from collections import deque
from time import sleep

import regex
from PIL import Image


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


def get_board(width: int, height: int, robot_positions: list[tuple[int, int]]) -> list[list[int]]:
    board: list[list[int]] = [[0 for _ in range(width)] for _ in range(height)]
    for pos in robot_positions:
        board[pos[1]][pos[0]] = 1
    return board


def print_board(width: int, height: int, robot_positions: list[tuple[int, int]]) -> None:
    board = get_board(width, height, robot_positions)
    for row in board:
        print(''.join(list(map(str, row))))


def get_flat_board(width: int, height: int, robot_positions: list[tuple[int, int]]) -> list[int]:
    board = get_board(width, height, robot_positions)
    flat_board: list[int] = []
    for row in board:
        for col in row:
            flat_board.append(col)
    return flat_board


def biggest_island_helper(robot_pos: tuple[int, int], robots_positions: set[tuple[int, int]],
                          visited: set[tuple[int, int]]) -> int:
    pos_stack: deque[tuple[int, int]] = deque([robot_pos])

    size = 0

    while len(pos_stack) != 0:
        robot_pos = pos_stack.pop()

        if robot_pos not in robots_positions or robot_pos in visited:
            continue

        visited.add(robot_pos)

        size += 1

        for direction in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            pos_stack.append((robot_pos[0] + direction[0], robot_pos[1] + direction[1]))

    return size


def biggest_island(robots_positions: set[tuple[int, int]]) -> int:
    visited = set()

    max_size = 0
    for robot_pos in robots_positions:
        max_size = max(max_size, biggest_island_helper(robot_pos, robots_positions, visited))

    return max_size


def robot_positions_after_time(robots_info: list[tuple[tuple[int, int], tuple[int, int]]], width: int, height: int,
                               time_s: int) -> list[tuple[int, int]]:
    positions_after_time: list[tuple[int, int]] = []
    # Calculate positions after 100 seconds
    for robot_info in robots_info:
        pos, vel = robot_info
        x = (pos[0] + vel[0] * time_s) % width
        y = (pos[1] + vel[1] * time_s) % height
        positions_after_time.append((x, y))

    return positions_after_time


def part1():
    time_s = 100
    width, height = 101, 103
    robots_info = load_robots_info('input.txt')
    robots_in_quadrant: list[int] = [0, 0, 0, 0]

    # Calculate positions after 100 seconds
    updated_positions = robot_positions_after_time(robots_info, width, height, time_s)
    for pos in updated_positions:
        # Get quadrant
        quadrant = pos_to_quadrant(width, height, pos[0], pos[1])
        if quadrant != -1:
            robots_in_quadrant[quadrant] += 1

    return functools.reduce(operator.mul, robots_in_quadrant, 1)


def part2(max_time_s: int, nr_boards_to_print: int):
    nr_boards_to_print = min(nr_boards_to_print, max_time_s)
    width, height = 101, 103
    robots_info = load_robots_info('input.txt')

    updated_positions: set[tuple[int, int]]
    # (size_of_island, time_s)
    max_islands_board_times: list[tuple[int, int]] = []

    for time_s in range(max_time_s):
        updated_positions = set(robot_positions_after_time(robots_info, width, height, time_s))

        max_size_island = biggest_island(updated_positions)
        heapq.heappush(max_islands_board_times, (-max_size_island, time_s))

    # Print 10 boards with biggest islands
    for i in range(nr_boards_to_print):
        max_island_size, time_s = heapq.heappop(max_islands_board_times)
        print(max_island_size, time_s)
        img = Image.new('1', (101, 103), 0)
        positions_after_time = robot_positions_after_time(robots_info, width, height, time_s)
        img.putdata(get_flat_board(width=101, height=103, robot_positions=positions_after_time))
        img.save(f'imgs/{abs(max_island_size)}-{time_s}.png')


print(part1())
part2(10000, 10)
