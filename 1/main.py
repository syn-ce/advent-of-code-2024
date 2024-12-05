l1 = []
l2 = []
with open('input.txt', 'r') as file:
    for line in file:
        n1, n2 = line.split()
        l1.append(int(n1))
        l2.append(int(n2))

l1.sort()
l2.sort()

diff = sum([abs(n1 - n2) for n1, n2 in zip(l1, l2)])

print(diff)

l1_frequencies = {}

for num in l1:
    l1_frequencies[num] = l1_frequencies.get(num, 0) + 1

similarity_score = sum([num * l1_frequencies.get(num, 0) for num in l2])
print(similarity_score)
