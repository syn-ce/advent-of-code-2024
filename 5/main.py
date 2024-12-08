from functools import cmp_to_key


def correct_order(nums: list[int], forbidden_successors: dict[int, set[int]]) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] in forbidden_successors and nums[j] in forbidden_successors[nums[i]]:
                return False
    return True


def parse_rules_and_prints(file_name: str) -> tuple[dict[int, set[int]], list[list[int]]]:
    lines: list[str]
    with open(file_name, 'r') as file:
        lines = file.read().split('\n')

    forbidden_successors: dict[int, set[int]] = dict()
    i = 0  # Parse rules
    while i < len(lines) and lines[i] != '':
        n1, n2 = [int(n) for n in lines[i].split('|')]
        if n2 not in forbidden_successors:
            forbidden_successors[n2] = set()
        forbidden_successors[n2].add(n1)
        i += 1

    i += 1  # Skip empty line

    # Parse prints
    prints: list[list[int]] = []
    while i < len(lines):
        nums = [int(n) for n in lines[i].split(',')]
        prints.append(nums)
        i += 1

    return forbidden_successors, prints


def part1():
    forbidden_successors, prints = parse_rules_and_prints('input.txt')

    middle_sum = 0
    # Check prints (naively, O(n^2))
    for nums in prints:
        if correct_order(nums, forbidden_successors):
            middle_sum += nums[len(nums) // 2]

    return middle_sum


def part2():
    forbidden_successors, prints = parse_rules_and_prints('input.txt')

    middle_sum_unordered = 0
    # Check prints (naively, O(n^2))
    for nums in prints:
        if not correct_order(nums, forbidden_successors):
            nums_sorted = sorted(nums, key=cmp_to_key(
                lambda a, b: -1 if a in forbidden_successors and b in forbidden_successors[a] else 1))
            middle_sum_unordered += nums_sorted[len(nums_sorted) // 2]

    return middle_sum_unordered


print(part1())
print(part2())
