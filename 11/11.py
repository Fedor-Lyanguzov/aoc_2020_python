from copy import deepcopy

with open("input") as f:
    _field = [list(s) for s in f.read().strip().split("\n")]

field = deepcopy(_field)
H = len(field)
W = len(field[0])

new_field = [['.' for _ in range(W)] for _ in range(H)]
directions = [
        ( 1,  1),
        ( 1,  0),
        ( 1, -1),
        ( 0,  1),
        ( 0, -1),
        (-1,  1),
        (-1,  0),
        (-1, -1),
        ]

change = True
while change:
    change = False
    for i, row in enumerate(field):
        for j, cell in enumerate(row):
            cn = 0
            for di, dj in directions:
                ii, jj = i+di, j+dj
                if 0<=ii<H and 0<=jj<W and field[ii][jj]=='#':
                    cn+=1
            if cell=='L' and cn==0:
                new_field[i][j] = '#'
                change = True
            elif cell=='#' and cn>=4:
                new_field[i][j] = 'L'
                change = True
            else:
                new_field[i][j] = cell
    field, new_field = new_field, field

print(sum(1 for row in field for cell in row if cell=='#'))

field = deepcopy(_field)
new_field = [['.' for _ in range(W)] for _ in range(H)]
change = True
while change:
    change = False
    for i, row in enumerate(field):
        for j, cell in enumerate(row):
            cn = 0
            for di, dj in directions:
                for l in range(1, max(H, W)+1):
                    ii, jj = i+di*l, j+dj*l
                    if 0<=ii<H and 0<=jj<W:
                        c = field[ii][jj]
                        if c=='#':
                            cn+=1
                            break
                        elif c=='L':
                            break
            if cell=='L' and cn==0:
                new_field[i][j] = '#'
                change = True
            elif cell=='#' and cn>=5:
                new_field[i][j] = 'L'
                change = True
            else:
                new_field[i][j] = cell
    field, new_field = new_field, field

print(sum(1 for row in field for cell in row if cell=='#'))
