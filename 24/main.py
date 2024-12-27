import operator
from typing import Callable


def load_circuit(filename: str):
    with open(filename) as file:
        lines = file.read().splitlines()

    wire_values: dict[str, int] = {}

    i = 0
    # Parse wire values
    while i < len(lines):
        if lines[i] == '':
            break
        s = lines[i].split(':')
        wire, value = s[0], int(s[1][-1])
        wire_values[wire] = value
        i += 1

    i += 1

    # Parse connections
    # (in_wire1, (op, in_wire2, out_wire))
    connections: dict[str, set[tuple[Callable[[int, int], int], str, str]]] = dict()

    while i < len(lines):
        s = lines[i].split(' ')
        in_wire1, op_type, in_wire2, out_wire = s[0], s[1], s[2], s[4]
        op = operator.and_ if op_type == 'AND' else (operator.or_ if op_type == 'OR' else operator.xor)
        if in_wire1 not in connections:
            connections[in_wire1] = set()
        if in_wire2 not in connections:
            connections[in_wire2] = set()
        connections[in_wire1].add((op, in_wire2, out_wire))  # Add to both in_wires (makes simulation easier)
        connections[in_wire2].add((op, in_wire1, out_wire))
        i += 1

    return wire_values, connections


def part1():
    wire_values, connections = load_circuit('input.txt')

    new_wire_values = set(wire_values.keys())

    # Calculate values for all wires
    while len(new_wire_values) > 0:
        next_new_wire_values = set()
        for wire in new_wire_values:  # Try to activate all connections of that wire
            for connection in connections.get(wire, set()):
                op, wire2, out_wire = connection
                if out_wire in wire_values or wire2 not in wire_values:  # Already know out or don't know in
                    continue
                out_wire_value = op(wire_values[wire], wire_values[wire2])
                wire_values[out_wire] = out_wire_value
                next_new_wire_values.add(out_wire)
        new_wire_values = next_new_wire_values

    # Collect wires starting with 'z'
    z_wires = []
    for wire in wire_values:
        if wire[0] == 'z':
            z_wires.append(wire)
    z_wires.sort(reverse=True)

    # Calc output
    res = 0
    for z_wire in z_wires:
        res = res * 2 + wire_values[z_wire]
    return res


print(part1())
