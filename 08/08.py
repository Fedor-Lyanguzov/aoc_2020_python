
with open('input') as f:
    code = {i: tuple(line.split(" ")) for i, line in enumerate(f.read().strip().split("\n"))}

def run(code):
    try:
        acc = 0
        pc = 0
        while True:
            op, value = code[pc]
            del code[pc]
            if op == 'acc':
                acc += int(value)
                pc += 1
            if op == 'nop':
                pc += 1
            if op == 'jmp':
                pc += int(value)
    except KeyError as e:
        return pc, acc

print(run(code.copy())[1])

m = max(code)
for i in code:
    if code[i][0] in ["nop", "jmp"]:
        new_code = code.copy()
        op, value = code[i]
        new_code[i] = ("nop" if op=="jmp" else "jmp", value)
        pc, acc = run(new_code)
        if pc==m+1:
            print(acc)
