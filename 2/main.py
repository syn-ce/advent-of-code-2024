safe_records = 0

with open('input.txt', 'r') as file:
    for line in file:
        record = line.split()
        increasing = int(record[0]) < int(record[1])  # Assumes at least two numbers in record

        safe = True

        for i in range(len(record) - 1):
            n1, n2 = int(record[i]), int(record[i + 1])
            if not increasing:
                n1, n2 = n2, n1
            if n1 >= n2 or n2 - n1 > 3:
                safe = False
                break

        if safe:
            safe_records += 1

print(safe_records)
