safe_records = 0


def valid_step(n1: int, n2: int, increasing: bool) -> bool:
    if not increasing:
        n1, n2 = n2, n1
    if n1 >= n2 or n2 - n1 > 3:
        return False
    return True


with open('input.txt', 'r') as file:
    for line in file:
        record = line.split()
        record = [int(n) for n in record]
        increasing = record[0] < record[1]  # Assumes at least two numbers in record

        safe = True
        removed_level = False

        # When encountering a problematic step (between n1 and n2),
        # test if removing n1 or n2 works locally, i.e. restores the order
        # Also need to reevaluate whether we are increasing or decreasing
        i = 0
        while i < len(record) - 1:
            n1, n2 = record[i], record[i + 1]
            if not valid_step(n1, n2, increasing):
                if removed_level:
                    safe = False
                    break

                removed_level = True
                if i >= len(record) - 2 or valid_step(n1, record[i + 2], increasing):
                    # TODO: check if below check (or something similar) is necessary
                    # or (i == 0 and valid_step(n1, record[i + 2], not increasing)):  # Remove n2
                    if i == 0:  # n2 is record[1] -> Reevaluate increasing
                        increasing = record[0] < record[2]
                    i += 1  # Skip n2
                elif i == 0:  # Remove n1
                    increasing = record[1] < record[2]  # n1 is record[0] -> Reevaluate increasing
                elif valid_step(record[i - 1], n2, increasing) or (
                        i == 1 and valid_step(record[i - 1], n2, not increasing)):  # Remove n1
                    if i == 1:  # n1 is record[0] -> Reevaluate increasing
                        increasing = record[0] < record[2]
                else:
                    safe = False
                    break
            i += 1

        if safe:
            safe_records += 1

print(safe_records)
