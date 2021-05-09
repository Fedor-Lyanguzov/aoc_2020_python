
with open("input") as f:
    t, buses = f.read().strip().split("\n")
    t = int(t)
    buses = buses.split(',')

first = map(int, filter(lambda x: x!='x', buses))
a, b = min((x-t%x, x) for x in first)
print(a*b)

# https://en.wikipedia.org/wiki/Chinese_remainder_theorem



