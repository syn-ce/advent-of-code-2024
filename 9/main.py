def read_uncompress_disk_map(file_name: str) -> list[int]:
    disk_map: list[int]

    with open(file_name) as file:
        disk_map = list(map(int, file.read().strip()))

    uncompressed_disk = []
    for i in range(len(disk_map)):
        val = -1  # free space
        if i & 1 == 0:
            val = i // 2  # file_id
        for j in range(disk_map[i]):
            uncompressed_disk.append(val)

    return uncompressed_disk


def part1():
    uncompressed_disk = read_uncompress_disk_map("input.txt")

    l, r = 0, len(uncompressed_disk) - 1
    while l < r:
        # Find free space with l
        while l < r and uncompressed_disk[l] != -1:
            l += 1
        # Find file block with r
        while l < r and uncompressed_disk[r] == -1:
            r -= 1
        uncompressed_disk[l], uncompressed_disk[r] = uncompressed_disk[r], uncompressed_disk[l]
        l += 1

    checksum = 0
    for i in range(len(uncompressed_disk)):
        if uncompressed_disk[i] == -1:
            break
        checksum += i * uncompressed_disk[i]

    return checksum


def part2():
    uncompressed_disk = read_uncompress_disk_map("input.txt")

    # Naive approach
    # entries (idx, size)
    free_spaces: list[tuple[int, int]] = []

    i = 0
    while i < len(uncompressed_disk):
        free_space = 0
        while i < len(uncompressed_disk) and uncompressed_disk[i] == -1:
            free_space += 1
            i += 1
        if free_space > 0:
            free_spaces.append((i - free_space, free_space))
        i += 1

    l, r = free_spaces[0][0], len(uncompressed_disk) - 1
    while l < r:
        # TODO: optimize this (actually remove 'free_space's with no space left)
        l = free_spaces[0][0]  # Leftmost free space
        # Find file block with r
        while l < r and uncompressed_disk[r] == -1:
            r -= 1
        if l >= r:
            break
        # Check size of r
        file_size = 1
        for p in range(r - 1, 0, -1):
            if uncompressed_disk[p] != uncompressed_disk[r]:  # Reached start of file
                break
            file_size += 1

        # Try to find free space big enough to accommodate file
        for i in range(len(free_spaces)):
            idx, free_space = free_spaces[i][0], free_spaces[i][1]
            if idx > r - file_size:
                break
            if file_size <= free_space:
                # Move file into free space, shrink free space
                for j in range(file_size):
                    uncompressed_disk[idx + j] = uncompressed_disk[r - file_size + 1 + j]
                    uncompressed_disk[r - file_size + 1 + j] = -1
                free_spaces[i] = (idx + file_size, free_space - file_size)
                break

        # Either file has not been moved (-> skip it) OR file has been moved (-> skip the free space it left)
        r -= file_size

    checksum = 0
    for i in range(len(uncompressed_disk)):
        if uncompressed_disk[i] == -1:
            continue
        checksum += i * uncompressed_disk[i]

    return checksum


print(part1())
print(part2())
