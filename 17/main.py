import math
from typing import Callable


# Combo operands:
# 0-3: literals
# 4: A
# 5: B
# 6: C
# 7: invalid


# Each instruction reads 3-bit number after it as its operand
# Instruction pointer increases by two every instruction (except for jumps)
# If PC tries to read opcode past end of program, it halts

# 0 (adv) -> A = trunc(A / (2**combo))
# 1 (bxl) -> B = B XOR instructions literal operand
# 2 (bst) -> B = combo % 8
# 3 (jnz) -> if A == 0: nothing; otherwise: instruction pointer to value of its literal operand (no incr. by 2)
# 4 (bxc) -> B = B XOR C (still reads operand, but ignores it)
# 5 (out) -> output: combo % 8
# 6 (bvd) -> B = trunc(A / (2**combo))
# 7 (cdv) -> C = trunc(A / (2**combo))

def div(combo_op_values: list[int], combo_op: int, instr_pointer: int, reg_ix: int):
    combo_op_values[reg_ix] = math.trunc(combo_op_values[4] / (2 ** combo_op_values[combo_op]))
    return instr_pointer + 2


def adv(combo_op_values: list[int], combo_op: int, instr_pointer: int, output: list[int]):
    return div(combo_op_values, combo_op, instr_pointer, 4)


def bxl(combo_op_values: list[int], combo_op: int, instr_pointer: int, output: list[int]):
    combo_op_values[5] = combo_op_values[5] ^ combo_op
    return instr_pointer + 2


def bst(combo_op_values: list[int], combo_op: int, instr_pointer: int, output: list[int]):
    combo_op_values[5] = combo_op_values[combo_op] % 8
    return instr_pointer + 2


def jnz(combo_op_values: list[int], combo_op: int, instr_pointer: int, output: list[int]):
    if combo_op_values[4] == 0:
        return instr_pointer + 2
    return combo_op


def bxc(combo_op_values: list[int], combo_op: int, instr_pointer: int, output: list[int]):
    combo_op_values[5] = combo_op_values[5] ^ combo_op_values[6]
    return instr_pointer + 2


def out(combo_op_values: list[int], combo_op: int, instr_pointer: int, output: list[int]):
    output.append(combo_op_values[combo_op] % 8)
    return instr_pointer + 2


def bdv(combo_op_values: list[int], combo_op: int, instr_pointer: int, output: list[int]):
    return div(combo_op_values, combo_op, instr_pointer, 5)


def cdv(combo_op_values: list[int], combo_op: int, instr_pointer: int, output: list[int]):
    return div(combo_op_values, combo_op, instr_pointer, 6)


InstructionFunction = Callable[[list[int], int, int, list[int]], int]

instructions: list[InstructionFunction] = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]


def load_program(filename: str) -> tuple[int, int, int, list[int]]:
    lines: list[str] = []
    with open(filename) as file:
        for line in file:
            lines.append(line)

    a, b, c = [int(lines[i].strip()[lines[i].find(':') + 2:]) for i in range(3)]

    program = list(map(int, lines[4].strip()[lines[4].find(':') + 2:].split(',')))

    return a, b, c, program


def parse(a: int, b: int, c: int, program: list[int]):
    combo_op_values: list[int] = [i for i in range(7)]
    combo_op_values[4] = a
    combo_op_values[5] = b
    combo_op_values[6] = c
    output: list[int] = []

    instr_pointer = 0

    while instr_pointer < len(program):
        instr, combo_op = program[instr_pointer], program[instr_pointer + 1]
        print(f'{instr_pointer}: instr {instr} ({instructions[instr].__name__}), operand {combo_op}')
        instr_pointer = instructions[instr](combo_op_values, combo_op, instr_pointer, output)
        print(f'Now: {combo_op_values}')

    return ','.join(map(str, output))


def part1():
    a, b, c, program = load_program('input.txt')
    return parse(a, b, c, program)


print(part1())
