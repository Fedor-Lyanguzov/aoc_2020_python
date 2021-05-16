from math import prod

with open('input') as f:
    rules, my_ticket, other = f.read().strip().split("\n\n")

rules = dict([r.split(': ') for r in rules.strip().split("\n")])
my_ticket = list(map(int, my_ticket.strip().split("\n")[1].split(',')))
other = [list(map(int, ticket.split(','))) for ticket in other.strip().split("\n")[1:]]

class Condition:
    def __init__(self, xs, xe, ys, ye):
        self.xs = xs
        self.xe = xe
        self.ys = ys
        self.ye = ye
    
    @classmethod
    def from_str(cls, s):
        l = [int(y) for x in s.split(" or ") for y in x.split('-')]
        return cls(*l)

    def __call__(self, x):
        return self.xs<=x<=self.xe or self.ys<=x<=self.ye
    def __str__(self):
        return f'{self.xs}<=x<={self.xe} or {self.ys}<=x<={self.ye}'
    __repr__ = __str__

rules = {k: Condition.from_str(v) for k, v in rules.items()}


valid_tickets = []
k = 0
for ticket in other:
    valid = True
    for value in ticket:
        f_valid = False
        for f in rules.values():
            if f(value):
                f_valid = True
        if not f_valid:
            valid = False
            k += value
    if valid:
        valid_tickets.append(ticket)

print(k)

trans = {i: k for i, k in enumerate(rules.keys())}
soup = [[[None 
    for _ in range(len(trans))] 
    for _ in range(len(valid_tickets[0]))] 
    for _ in range(len(valid_tickets))]
for i_t, ticket in enumerate(valid_tickets):
    for i_v, value in enumerate(ticket):
        for i_f, k in trans.items():
            soup[i_t][i_v][i_f] = rules[k](value)


rev_trans = {i: [] for i in range(len(valid_tickets[0]))}
for i_vv in range(len(valid_tickets[0])):
    for i_f in trans:
        valid = True
        for i_t in range(len(valid_tickets)):
            if not soup[i_t][i_vv][i_f]: 
                valid = False
                break
        if valid:
            rev_trans[i_vv].append(trans[i_f])
rev_trans = sorted([(i, set(f)) for i, f in rev_trans.items()], key=lambda x: len(x[1]))
d = {}
e = set()
for i, f in rev_trans:
    d[i] = f-e
    e = e|f
print(prod(my_ticket[i] for i, f in d.items() if 'departure' in list(f)[0]))

print("done")
