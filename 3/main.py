import re

sum_of_muls = 0

with open('input.txt', 'r') as file:
    s = file.read()
    dos_donts_muls = re.findall(re.compile("(mul\(\d+,\d+\))|(do\(\))|(don't\(\))"), s)
    print(dos_donts_muls)
    do = True

    for instruction in dos_donts_muls:
        if instruction[0] != '':  # mul(x,y)
            if not do:
                continue
            mul_split = instruction[0].split(',')
            n1 = int(mul_split[0][4:])
            n2 = int(mul_split[1][:-1])
            sum_of_muls += n1 * n2
        elif instruction[2] != '':  # don't()
            do = False
        else:  # do()
            do = True

print(sum_of_muls)
