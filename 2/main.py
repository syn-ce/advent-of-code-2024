def valid_step(n1: int, n2: int, increasing: bool) -> bool:
    if not increasing:
        n1, n2 = n2, n1
    return n1 < n2 and n2 - n1 <= 3


safe_records = 0

with open('input.txt', 'r') as file:
    for line in file:
        record = line.split()
        record = [int(n) for n in record]

        # Determine whether increasing or decreasing (for 2 of 24 configs,
        # we can't restore a sequence by eliminating just one number, but in
        # that case we don't care since we'll fail anyway) ((3,1,4,2) and (3,4,1,2))
        increasing = (int(record[0] < record[1]) + int(record[1] < record[2]) + int(
            record[2] < record[3])) > 1  # Assumes at least four numbers in record

        safe = True
        removed_level = False

        # When encountering a problematic step (between n1 and n2),
        # test if removing n1 or n2 works locally, i.e. restores the order
        i = 0
        while i < len(record) - 1:
            n1, n2 = record[i], record[i + 1]
            if not valid_step(n1, n2, increasing):
                if removed_level:
                    safe = False
                    break
                removed_level = True
                if i >= len(record) - 2 or valid_step(n1, record[i + 2], increasing):  # Remove n2
                    i += 1  # Skip n2
                elif i != 0 and not valid_step(record[i - 1], n2, increasing):  # Also can't remove n1
                    safe = False
                    break
            i += 1

        if safe:
            safe_records += 1

print(safe_records)
