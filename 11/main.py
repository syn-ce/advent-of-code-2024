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


def part1():
    stones = read_stones('input.txt')
    for _ in range(25):
        nr_stones = len(stones)
        for j in range(nr_stones):
            stone = stones[j]
            stone1, stone2 = apply_blink(stone)
            stones[j] = stone1
            if stone2 != -1:
                stones.append(stone2)

    return len(stones)


print(part1())
