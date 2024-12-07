# Advent of Code 2024

| Day       | Part 1 approach                                                                             | Time&#x2011;C. | Space&#x2011;C. | Part 2 approach                                                                | Time&#x2011;C. | Space&#x2011;C. |
|-----------|---------------------------------------------------------------------------------------------|----------------|-----------------|--------------------------------------------------------------------------------|----------------|-----------------|
| 1         | sort both lists, add diffs between pairs                                                    | $n \log n$     | $1^{1}$         | count frequencies in right list in map, multiply with nums from left           | $n$            | $n$             |
| 2         | determine if in-/decreasing with first 2 numbers, check all nums accordingly                | $n$            | $1$             | determine if in-/decreasing with first 4 numbers, try removing first bad level | $n$            | $1$             |
| 3         | regex `mul\(\d+,\d+\)`, add products                                                        | $n$            | $1$             | regex `(mul\(\d+,\d+\))\|(do\(\))\|(don't\(\))`, (de)activate, add products    | $n$            | $1$             |
| 4 $^{*2}$ | for every cell: search in all directions, maintain dir once started                         | $n$            | $1$             | find cells which are middle 'A' of two diagonal 'MAS'                          | $n$            | $n$             |
| 5         | naive: store forbidden successors in map, for every num check if any successor is forbidden | $n$            | $n$             | take incorrectly-ordered, sort using custom comparator based on parsed rules   | $n\log n)$     | $1^1$           |
| 6 $^{*2}$ | simulation until guard leaves board                                                         | $n$            | $1$             | naive: for every visited cell: try placing obstruction, check for cycle        | $n^2$          | $n$             |
| 7 $^{*2}$ | backtrack with add and mul                                                                  | $2^n$          | $n$             | backtrack with add, mul and concat                                             | $3^n$          | $n$             |

$^{*1}$ actually $O(n)$ in Python because of sorting.
$^{*2}$ $n$ is the size (nr of cells) of the board
