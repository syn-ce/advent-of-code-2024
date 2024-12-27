def load_locks_keys(filename: str):
    locks, keys = [], []

    with open(filename) as file:
        lines = file.read().splitlines()

    # Assumes all keys and locks to be of same length
    length = len(lines[0])
    for i in range(0, len(lines), 8):
        nums = [0 for _ in range(length)]
        for col in range(length):
            for row in range(7):
                if lines[i + row][col] == '#':
                    nums[col] += 1

        if lines[i][0] == '#':  # Lock
            locks.append(tuple(nums))
        else:  # Key
            keys.append(tuple(nums))

    return locks, keys


def part1():
    locks, keys = load_locks_keys('input.txt')

    fitting_pairs = 0

    for lock in locks:
        for key in keys:
            fit = True
            for i in range(len(lock)):
                if lock[i] + key[i] > 7:
                    fit = False
                    break
            if fit:
                fitting_pairs += 1

    return fitting_pairs


print(part1())
