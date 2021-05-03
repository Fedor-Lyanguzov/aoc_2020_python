
with open("input") as f:
    data = f.read().strip().split("\n")

# light beige bags contain 5 dark green bags, 5 light gray bags, 3 faded indigo bags, 2 vibrant aqua bags.
def f(bag):
    count, *color = bag.split(' ')[:-1]
    color = ' '.join(color)
    return count, color
    
rules = {}
for rule in data:
    bag, value = rule.split(" bags contain ")
    if value=="no other bags.":
        values = {}
    else:
        values = value[:-1].split(", ")
        values = {color: int(count) for count, color in map(f, values)}
    rules[bag] = values

from functools import cache
@cache
def shiny_gold(bag):
    global count
    if "shiny gold" in rules[bag]:
        return True
    if any(shiny_gold(inner) for inner in rules[bag].keys()):
        return True
    return False

print(len({bag for bag in rules if shiny_gold(bag)}))

def inside(bag):
    if not rules[bag]:
        return 1
    return 1+sum(count*inside(inner) for inner, count in rules[bag].items())
print(inside("shiny gold")-1)
