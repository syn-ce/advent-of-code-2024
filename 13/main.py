import regex

type equation = tuple[int, int, int]


def load_equations(file_name: str) -> list[tuple[equation, equation]]:
    equations: list[tuple[equation, equation]] = []

    with open(file_name) as file:
        lines = file.read().splitlines()

    for i in range(0, len(lines), 4):
        x1, y1 = list(map(int, regex.findall('\\d+', lines[i])))
        x2, y2 = list(map(int, regex.findall('\\d+', lines[i + 1])))
        res1, res2 = list(map(int, regex.findall('\\d+', lines[i + 2])))
        eq1 = (x1, x2, res1)
        eq2 = (y1, y2, res2)
        equations.append((eq1, eq2))

    return equations


def min_tokens_for_solvable(equations: list[tuple[equation, equation]]) -> int:
    tokens = 0
    for equation_pair in equations:
        eq1, eq2 = equation_pair  # Assumes unique solution to exist
        b = (eq2[0] * eq1[2] - eq1[0] * eq2[2]) / (eq1[1] * eq2[0] - eq2[1] * eq1[0])
        a = (eq1[2] - eq1[1] * b) / eq1[0]
        if a % 1 == 0 and b % 1 == 0:
            tokens += int(3 * a + b)

    return tokens


def part1():
    equations = load_equations('input.txt')
    return min_tokens_for_solvable(equations)


def part2():
    equations = load_equations('input.txt')
    for i in range(len(equations)):
        eq1, eq2 = equations[i]
        equations[i] = ((eq1[0], eq1[1], eq1[2] + 10000000000000), (eq2[0], eq2[1], eq2[2] + 10000000000000))
    return min_tokens_for_solvable(equations)


print(part1())
print(part2())
