import math
from typing import Callable
import operator


def load_equations(file_name: str) -> list[tuple[int, list[int]]]:
    equations: list[tuple[int, list[int]]] = []

    with open(file_name, 'r') as file:
        for line in file:
            target, *nums = line.split()
            target = int(target[:-1])  # Remove colon
            nums = list(map(int, nums))
            equations.append((target, nums))

    return equations


def backtrack_operations(target: int, cur: int, nums: list[int], idx: int,
                         operators: list[Callable[[int, int], int]], op_idx: int) -> bool:
    if idx == len(nums):
        return cur == target

    # Apply operator
    cur = operators[op_idx](cur, nums[idx])

    if cur > target:  # Assumes all nums to be strictly positive, all ops to yield positive results
        return False

    # (Lazily) try (all) operators for next position
    return any(backtrack_operations(target, cur, nums, idx + 1, operators, op_ix) for op_ix in range(len(operators)))


# Assumes all nums to be strictly positive
def fit_equations_with_operators(operators: list[Callable[[int, int], int]]):
    total = 0
    equations = load_equations('input.txt')
    for target, nums in equations:
        # Try all combinations
        if any(backtrack_operations(target, nums[0], nums, 1, operators, op_ix) for op_ix in range(len(operators))):
            total += target

    return total


def part1():
    operators = [operator.add, operator.mul]
    total = fit_equations_with_operators(operators)
    return total


def part2():
    concat: Callable[[int, int], int] = lambda a, b: pow(10, int(math.ceil(math.log10(b + 1)))) * a + b
    operators = [operator.add, operator.mul, concat]
    total = fit_equations_with_operators(operators)
    return total


print(part1())
print(part2())
