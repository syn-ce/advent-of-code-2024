from typing import Callable
import operator


def backtrack_operations(target: int, cur: int, nums: list[int], idx: int,
                         operation: Callable[[int, int], int]) -> bool:
    if idx == len(nums):
        return cur == target

    # Apply operation
    cur = operation(cur, nums[idx])

    # Try both operations for next position
    return (backtrack_operations(target, cur, nums, idx + 1, operator.add)
            or backtrack_operations(target, cur, nums, idx + 1, operator.mul))


with open("input.txt", 'r') as file:
    total = 0
    for line in file:
        target, *nums = line.split()
        target = int(target[:-1])  # Remove colon
        nums = list(map(int, nums))

        # Try all combinations
        if (backtrack_operations(target, nums[0], nums, 1, operator.add)
                or backtrack_operations(target, nums[0], nums, 1, operator.mul)):
            total += target

    print(total)
