data = [(s[0], int(s[1:])) for s in """
F10
N3
F7
R90
F11
""".strip().split("\n")]
with open("input") as f:
    data = [(s[0], int(s[1:])) for s in f.read().strip().split("\n")]

ship = (0, 0, 0)

directions = {
        0: (1, 0),
        90: (0, 1),
        180: (-1, 0),
        270: (0, -1),
        }

def move(dx, dy, ship):
    x, y, a = ship
    return (x+dx, y+dy, a)

def turn(sign, degree, ship):
    x, y, a = ship
    return (x, y, (a+sign*degree)%360)

def moveF(value, ship):
    x, y, a = ship
    dx, dy = directions[a]
    dx, dy = dx*value, dy*value
    return move(dx, dy, ship)

funcs = {
        "L": lambda degree, ship: turn(1, degree, ship),
        "R": lambda degree, ship: turn(-1, degree, ship),
        "N": lambda value, ship: move(0, value, ship),
        "S": lambda value, ship: move(0, -value, ship),
        "E": lambda value, ship: move(value, 0, ship),
        "W": lambda value, ship: move(-value, 0, ship),
        "F": moveF,
        }

for op, value in data:
    ship = funcs[op](value, ship)

x, y, _ = ship
print(abs(x)+abs(y))



def turn90(waypoint):
    x, y = waypoint
    return (-y, x)
def turn(sign, degree, waypoint):
    for _ in range((360+sign*degree)%360//90):
        waypoint = turn90(waypoint)
    return waypoint
def moveF(value, waypoint, ship):
    dx, dy = waypoint
    x, y = ship
    return waypoint, (x+dx*value, y+dy*value)
def move(dx, dy, ship):
    x, y = ship
    return (x+dx, y+dy)
waypoint = (10, 1)
ship = (0, 0)

funcs = {
        "L": lambda degree, waypoint, ship: (turn(1, degree, waypoint), ship),
        "R": lambda degree, waypoint, ship: (turn(-1, degree, waypoint), ship),
        "N": lambda value, waypoint, ship: (move(0, value, waypoint), ship),
        "S": lambda value, waypoint, ship: (move(0, -value, waypoint), ship),
        "E": lambda value, waypoint, ship: (move(value, 0, waypoint), ship),
        "W": lambda value, waypoint, ship: (move(-value, 0, waypoint), ship),
        "F": moveF,
        }
for op, value in data:
    waypoint, ship = funcs[op](value, waypoint, ship)

x, y = ship
print(abs(x)+abs(y))
