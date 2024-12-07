# Advent of Code 2024

| Day       | Part 1 approach                                                                             | Time          | Space      | Part 2 approach                                                                | Time         | Space    |
|-----------|---------------------------------------------------------------------------------------------|---------------|------------|--------------------------------------------------------------------------------|--------------|----------|
| 1         | sort both lists, add diffs between pairs                                                    | $O(n \log n)$ | $O(1)^{1}$ | count frequencies in right list in map, multiply with nums from left           | $O(n)$       | $O(n)$   |
| 2         | determine if in-/decreasing with first 2 numbers, check all nums accordingly                | $O(n)$        | $O(1)$     | determine if in-/decreasing with first 4 numbers, try removing first bad level | $O(n)$       | $O(1)$   |
| 3         | regex `mul\(\d+,\d+\)`, add products                                                        | $O(n)$        | $O(1)$     | regex `(mul\(\d+,\d+\))\|(do\(\))\|(don't\(\))`, (de)activate, add products    | $O(n)$       | $O(1)$   |
| 4 $^{*2}$ | for every cell: search in all directions, maintain dir once started                         | $O(n)$        | $O(1)$     | find cells which are middle 'A' of two diagonal 'MAS'                          | $O(n)$       | $O(n)$   |
| 5         | naive: store forbidden successors in map, for every num check if any successor is forbidden | $O(n)$        | $O(n)$     | take incorrectly-ordered, sort using custom comparator based on parsed rules   | $O(n\log n)$ | $O(1)^1$ |
| 6 $^{*2}$ | simulation until guard leaves board                                                         | $O(n)$        | $O(1)$     | naive: for every visited cell: try placing obstruction, check for cycle        | $O(n^2)$     | $O(n)$   |
| 7 $^{*2}$ | backtrack with add and mul                                                                  | $O(2^n)$      | $O(n)$     | backtrack with add, mul and concat                                             | $O(3^n)$     | $O(n)$   |

$^{*1}$ actually $O(n)$ in Python because of sorting.
$^{*2}$ $n$ is the size (nr of cells) of the board
