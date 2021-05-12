from itertools import product

with open("input") as f:
    commands = f.read().strip().split("\n")

print(len(commands))

def prepare_command(c):
    a, b = c.split(" = ")
    if a == "mask":
        return ("mask", (b,))
    m = int(a[4:-1])
    b = int(b)
    return ("mem", (m, b))
commands = [prepare_command(command) for command in commands]

mem = {}
for op, par in commands:
    if op=="mask":
        m, = par
        or_mask = int(m.replace('X', "0"), base=2)
        and_mask = int(m.replace("X", "1"), base=2)
    elif op=="mem":
        add, val = par
        val = val & and_mask | or_mask
        mem[add] = val
    else:
        print("error")

print(sum(mem.values()))

mem = {}
for op, par in commands:
    if op=="mask":
        mask, = par
    elif op=="mem":
        add, val = par
        for comb in product(["0", "1"], repeat=mask.count("X")):
            or_mask = int(mask.replace("X", "0"), base=2)
            and_mask = int(mask.replace("0", "1").replace("X", "0"), base=2)
            _mask = int(mask.replace("X", "{}").format(*comb), base=2)
            _add = (add | or_mask) & and_mask | _mask
            mem[_add] = val
    else:
        print("error")
print(sum(mem.values()))
