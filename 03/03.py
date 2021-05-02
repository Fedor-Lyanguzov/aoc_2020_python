import re

with open('03-input') as f:
    landscape = [row.strip() for row in f]

count = 0
i, j = 0, 0
l = len(landscape[0])
while i<len(landscape):
    if landscape[i][j]=='#':
        count += 1
    i += 1
    j = (j+3)%l
print(count)

counts = []
for dx, dy in [(1,1), (3,1), (5,1), (7,1), (1, 2)]:
    count = 0
    i, j = 0, 0
    l = len(landscape[0])
    while i<len(landscape):
        if landscape[i][j]=='#':
            count += 1
        i += dy
        j = (j+dx)%l
    counts.append(count)

from math import prod
print(prod(counts))
