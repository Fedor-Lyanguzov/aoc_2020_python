
with open("input") as f:
    numbers = [int(x) for x in f.read().strip().split("\n")]
from itertools import combinations

for i, x in enumerate(numbers[25:], 25):
    window = numbers[i-25:i]
    is_valid = False
    for a, b in combinations(window, 2):
        if a+b==x:
            is_valid = True
    if not is_valid:
        break
print(x)

start = 0
end = 10
while (s := sum(numbers[start:end]))!=x:
    if s>x:
        start += 1
    if s<x:
        end += 1

print(min(numbers[start:end])+max(numbers[start:end]))
