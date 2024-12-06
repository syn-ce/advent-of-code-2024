import re

sum_of_muls = 0

with open('input.txt', 'r') as file:
    s = file.read()
    res = re.findall("mul\(\d+,\d+\)", s)

    for mul in res:
        mul_split = mul.split(',')
        n1 = int(mul_split[0][4:])
        n2 = int(mul_split[1][:-1])
        sum_of_muls += n1 * n2

print(sum_of_muls)