
with open('input') as f:
    data = f.read().strip().split('\n')

initial = {(j, i, 0) for i, s in enumerate(data) for j, c in enumerate(s) if c=='#'}

def fence(s):
    min_x = min(s, key=lambda x: x[0])[0]
    min_y = min(s, key=lambda x: x[1])[1]
    min_z = min(s, key=lambda x: x[2])[2]
    max_x = max(s, key=lambda x: x[0])[0]
    max_y = max(s, key=lambda x: x[1])[1]
    max_z = max(s, key=lambda x: x[2])[2]
    return (min_x-1, max_x+2), (min_y-1, max_y+2), (min_z-1, max_z+2)

def neighbours(s, x, y, z):
    n=0
    for _x in range(x-1, x+2):
        for _y in range(y-1, y+2):
            for _z in range(z-1, z+2):
                if not (_x==x and _y==y and _z==z):
                    if (_x, _y, _z) in s:
                        n+=1
    return n

for _ in range(6):
    new = set()
    r_x, r_y, r_z = fence(initial)
    for x in range(*r_x):
        for y in range(*r_y):
            for z in range(*r_z):
                n = neighbours(initial, x, y, z)
                if (x,y,z) in initial:
                    if n==2 or n==3:
                        new.add((x,y,z))
                else:
                    if n==3:
                        new.add((x,y,z))
    initial = new

print(len(initial))
                    
print('done')
