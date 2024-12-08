from fractions import Fraction


# One type of antenna:
# Fore every pair:
# Calculate distance as a vector between them, calculate positions of both antinodes
# Check whether antinodes are on map

def collect_antennas(file_name):
    with open(file_name, 'r') as file:
        antennas: dict[chr, list[(int, int)]] = dict()
        rows = 0
        cols = 0
        for row, line in enumerate(file):
            for col, ch in enumerate(line.strip()):
                if ch != '.':
                    if ch not in antennas:
                        antennas[ch] = []
                    antennas[ch].append((row, col))
            cols = len(line)
            rows += 1
        return antennas, rows, cols


def in_range(row_col: (int, int), rows: int, cols: int) -> bool:
    return 0 <= row_col[0] < rows and 0 <= row_col[1] < cols


def part1():
    antennas, rows, cols = collect_antennas('input.txt')

    # Pairs of same-type antennas create antidotes (might be out of bounds)
    antinodes: set[(int, int)] = set()
    for ant_type_positions in antennas.values():
        for i, ant_position1 in enumerate(ant_type_positions):
            for j in range(i + 1, len(ant_type_positions)):
                ant_position2 = ant_type_positions[j]
                yd, xd = ant_position2[1] - ant_position1[1], ant_position2[0] - ant_position1[0]
                new_antidones = [(ant_position1[1] - yd, ant_position1[0] - xd),
                                 (ant_position2[1] + yd, ant_position2[0] + xd)]
                for antinode in new_antidones:
                    if in_range(antinode, rows, cols):
                        antinodes.add(antinode)
    return len(antinodes)


def part2():
    antennas, rows, cols = collect_antennas('input.txt')

    antinodes: set[(int, int)] = set()
    for ant_type_positions in antennas.values():
        for i, ant_position1 in enumerate(ant_type_positions):
            for j in range(i + 1, len(ant_type_positions)):
                ant_position2 = ant_type_positions[j]
                yd, xd = ant_position2[1] - ant_position1[1], ant_position2[0] - ant_position1[0]
                frac = Fraction(yd, xd)  # Reduce fraction
                yd, xd = frac.numerator, frac.denominator
                dist = 0
                new_antinodes = [(ant_position1[1], ant_position1[0]),
                                 (ant_position2[1], ant_position2[0])]
                while any(in_range(antinode, rows, cols) for antinode in new_antinodes):
                    for antinode in new_antinodes:
                        if in_range(antinode, rows, cols):
                            antinodes.add(antinode)
                    dist += 1
                    new_antinodes = [(ant_position1[1] - yd * dist, ant_position1[0] - xd * dist),
                                     (ant_position2[1] + yd * dist, ant_position2[0] + xd * dist)]
    return len(antinodes)


print(part1())
print(part2())
