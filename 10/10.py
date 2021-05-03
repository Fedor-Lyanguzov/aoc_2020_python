
with open("input") as f:
    adapters = [int(x) for x in f.read().strip().split("\n")]

adapters.extend([0, max(adapters)+3])
adapters.sort()
joltages = [b-a for a, b in zip(adapters, adapters[1:])]
print(joltages.count(1)*joltages.count(3))


joltages = ''.join(str(x) for x in joltages)
joltages = joltages.split('3')

counts = {
        '': 1,
        '1': 1,
        '11': 2,
        '111': 4,
        '1111': 7,
        }
from functools import reduce
print(reduce(lambda x, y: x*counts[y], joltages, 1))

