def load_secrets(filename: str) -> list[int]:
    secrets = []
    with open(filename) as file:
        for line in file:
            secrets.append(int(line.strip()))
    return secrets


def mix(secret: int, num: int) -> int:
    return secret ^ num


def prune(secret: int) -> int:
    return secret % 16777216


def step(secret: int) -> int:
    secret = prune(mix(secret, secret * 64))
    secret = prune(mix(secret, secret // 32))
    return prune(mix(secret, secret * 2048))


def part1():
    secrets = load_secrets('input.txt')
    secret_sums = 0
    for secret in secrets:
        for _ in range(2000):
            secret = step(secret)
        secret_sums += secret
    return secret_sums


def part2():
    secrets = load_secrets('input.txt')
    sequence_to_profit: dict[tuple[int, int, int, int], int] = dict()

    for secret in secrets:
        seen = set()
        sequence = (0, 0, 0, 0)
        for i in range(2000):
            next_secret = step(secret)
            diff = next_secret % 10 - secret % 10
            sequence = (sequence[1], sequence[2], sequence[3], diff)
            secret = next_secret
            if i >= 3 and sequence not in seen:
                sequence_to_profit[sequence] = sequence_to_profit.get(sequence, 0) + (secret % 10)
                seen.add(sequence)

    k = max(sequence_to_profit, key=sequence_to_profit.get)
    print(k, sequence_to_profit[k])
    return max(sequence_to_profit.values())


print(part1())
print(part2())
