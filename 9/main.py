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


print(part1())
