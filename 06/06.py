
with open("input") as f:
    groups = [[x for x in group.split("\n")] for group in f.read().strip().split("\n\n")]

print(sum(len(set().union(*(set(person) for person in group))) for group in groups))
from functools import reduce
print(sum(len(reduce(set.intersection, (set(person) for person in group))) for group in groups))
