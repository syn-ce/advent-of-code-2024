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


print(part1())
