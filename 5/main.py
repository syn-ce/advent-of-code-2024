def correct_order(nums: list[int], forbidden_successors: dict[int, set[int]]) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] in forbidden_successors and nums[j] in forbidden_successors[nums[i]]:
                return False
    return True


with open("input.txt", 'r') as file:
    prints = []
    lines = file.read().split('\n')

    forbidden_successors: dict[int, set[int]] = dict()
    i = 0  # Parse rules
    while i < len(lines) and lines[i] != '':
        n1, n2 = [int(n) for n in lines[i].split('|')]
        if n2 not in forbidden_successors:
            forbidden_successors[n2] = set()
        forbidden_successors[n2].add(n1)
        i += 1
    i += 1

    middle_sum = 0
    # Check prints (naively, O(n^2))
    while i < len(lines):
        nums = [int(n) for n in lines[i].split(',')]
        if correct_order(nums, forbidden_successors):
            middle_sum += nums[len(nums) // 2]
        i += 1

    print(middle_sum)
