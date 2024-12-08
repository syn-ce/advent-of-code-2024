import re


def read_instructions(file_name: str) -> str:
    with open(file_name, 'r') as file:
        return file.read()


def part1():
    sum_of_muls = 0

    instructions = read_instructions('input.txt')
    muls = re.findall("mul\(\d+,\d+\)", instructions)

    for mul in muls:
        mul_split = mul.split(',')
        n1 = int(mul_split[0][4:])
        n2 = int(mul_split[1][:-1])
        sum_of_muls += n1 * n2

    return sum_of_muls


def part2():
    sum_of_muls = 0

    instructions = read_instructions('input.txt')
    dos_donts_muls = re.findall(re.compile("(mul\(\d+,\d+\))|(do\(\))|(don't\(\))"), instructions)
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
    return sum_of_muls


print(part1())
print(part2())
