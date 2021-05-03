
with open("input") as f:
    data = f.read().strip().split("\n")

seats = [int(s.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"), base=2) 
        for s in data]
print(max(seats))
print([(a+b)//2 for a, b in zip(sorted(seats), sorted(seats)[1:]) if b-a>1][0])
