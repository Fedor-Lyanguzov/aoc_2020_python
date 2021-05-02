from itertools import combinations

with open('01-input') as f:
    numbers = {int(row.strip()) for row in f}

for n in numbers:
    if 2020-n in numbers:
        print(n*(2020-n))


for a,b,c in combinations(numbers, 3):
    if a+b+c==2020:
        print(a*b*c)

