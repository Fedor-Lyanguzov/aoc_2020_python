from collections import defaultdict

numbers = [14,1,17,0,3,20]

def f(numbers, nth):
    d={}
    for i, n in enumerate(numbers[:-1], 1):
        d[n] = i

    prev = numbers[-1]
    for i in range(len(numbers), nth):
        if prev not in d:
            d[prev] = i
            prev = 0
        else:
            next = i-d[prev]
            d[prev] = i
            prev = next
    return prev

print(f(numbers, 2020))
print(f(numbers, 30_000_000))
