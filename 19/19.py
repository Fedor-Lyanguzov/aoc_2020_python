rules, data = """
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
""".replace('"a"', 'a').replace('"b"', 'b').strip().split("\n\n")

rules, data = """
42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
""".replace('"a"', 'a').replace('"b"', 'b').strip().split("\n\n")

with open('input') as f:
    rules, data = f.read().replace('"a"', 'a').replace('"b"', 'b').strip().split("\n\n") 

data = data.split("\n")
rules = dict(row.split(': ') for row in rules.split("\n"))

rules = {i: [rule.split() for rule in row.split(' | ')] for i, row in rules.items()}
print(len(data))

def f(s, r):
    if s=='':
        #print('1', s, r, False, 0)
        return False, 0
    if r in ['a', 'b']:
        if s[0]==r:
            #print('2', s, r, True, 1)
            return True, 1
        else:
            #print('3', s, r, False, 0)
            return False, 0
    res = False
    for seq_r in rules[r]:
        k = 0
        _s = s
        for rule in seq_r:
            c, _k = f(_s, rule)
            if not c: break
            _s = _s[_k:]
            k += _k
        else:
            res = True
            break
    #print('4', s, r, res, k)
    return res, k

print(sum(1 for d, (f, k) in zip(data, list(f(d, '0') for d in data)) if len(d)==k and f))



rules.update({'8': [['42'], ['42', '8']], '11': [['42', '31'], ['42', '11', '31']]})

print(sum(1 for d, (f, k) in zip(data, list(f(d, '0') for d in data)) if len(d)==k and f))

