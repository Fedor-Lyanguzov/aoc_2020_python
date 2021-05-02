import re

with open('02-input') as f:
    passwords = [row.strip() for row in f]

pattern = re.compile(r'(\d*)-(\d*) (\w): (.*)')
count = 0
for p in passwords:
    if m := pattern.match(p):
        n1, n2, l, p = m.groups()
        c = p.count(l)
        if int(n1)<=c<=int(n2):
            count += 1

print(count)

count = 0
for p in passwords:
    if m := pattern.match(p):
        n1, n2, l, p = m.groups()
        n1, n2 = int(n1)-1, int(n2)-1
        if p[n1]==l and p[n2]!=l or p[n1]!=l and p[n2]==l:
            count += 1

print(count)
