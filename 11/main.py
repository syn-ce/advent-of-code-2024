import math


def read_stones(file_name: str) -> list[int]:
    with open(file_name) as file:
        return list(map(int, file.read().split()))


def apply_blink(stone: int) -> tuple[int, int]:
    if stone == 0:
        return 1, -1

    nr_digits = int(math.ceil(math.log10(stone + 1)))
    if nr_digits % 2 == 0:
        base10exp = 10 ** (nr_digits // 2)
        stone1 = stone // base10exp
        return stone1, stone - stone1 * base10exp

    return stone * 2024, -1


def simulate_stone_blinking(nr_iterations: int) -> int:
    stone_counts: dict[int, int] = dict((stone, 1) for stone in read_stones('input.txt'))
    for _ in range(nr_iterations):
        new_stone_counts: dict[int, int] = dict()
        for stone, count in stone_counts.items():
            stone1, stone2 = apply_blink(stone)
            new_stone_counts[stone1] = new_stone_counts.get(stone1, 0) + count
            if stone2 != -1:
                new_stone_counts[stone2] = new_stone_counts.get(stone2, 0) + count
        stone_counts = new_stone_counts

    return sum(stone_counts.values())


def part1():
    return simulate_stone_blinking(25)


def part2():
    return simulate_stone_blinking(75)


print(part1())
print(part2())
