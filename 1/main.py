def read_sort_lists(file_name: str) -> tuple[list[int], list[int]]:
    l1 = []
    l2 = []
    with open(file_name, 'r') as file:
        for line in file:
            n1, n2 = line.split()
            l1.append(int(n1))
            l2.append(int(n2))
    l1.sort()
    l2.sort()
    return l1, l2


def part1():
    l1, l2 = read_sort_lists('input.txt')

    diff = sum([abs(n1 - n2) for n1, n2 in zip(l1, l2)])
    return diff


def part2():
    l1, l2 = read_sort_lists('input.txt')

    l1_frequencies = {}

    for num in l1:
        l1_frequencies[num] = l1_frequencies.get(num, 0) + 1

    similarity_score = sum([num * l1_frequencies.get(num, 0) for num in l2])
    return similarity_score


print(part1())
print(part2())
