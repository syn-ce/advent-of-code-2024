import math
from typing import Callable
import operator


def backtrack_operations(target: int, cur: int, nums: list[int], idx: int,
                         operators: list[Callable[[int, int], int]], op_idx: int) -> bool:
    if idx == len(nums):
        return cur == target

    # Apply operator
    cur = operators[op_idx](cur, nums[idx])

    if cur > target:  # Assumes all nums to be strictly positive
        return False

    # (Lazily) try (all) operators for next position
    return any(backtrack_operations(target, cur, nums, idx + 1, operators, op_ix) for op_ix in range(len(operators)))


with open("input.txt", 'r') as file:
    total = 0
    for line in file:
        target, *nums = line.split()
        target = int(target[:-1])  # Remove colon
        nums = list(map(int, nums))

        # Assumes all nums to be strictly positive
        operators = [operator.add, operator.mul, lambda a, b: pow(10, int(math.ceil(math.log10(b + 1)))) * a + b]
        # Try all combinations
        if any(backtrack_operations(target, nums[0], nums, 1, operators, op_ix) for op_ix in range(len(operators))):
            total += target

    print(total)
