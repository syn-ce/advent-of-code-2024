# One type of antenna:
# Fore every pair:
# Calculate distance as a vector between them, calculate positions of both antinodes
# Check whether antinodes are on map

with open('input.txt', 'r') as file:
    # Collect antennas
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
                    if 0 <= antinode[0] < rows and 0 <= antinode[1] < cols:
                        antinodes.add(antinode)
    print(len(antinodes))
