# http://rosettacode.org/wiki/Parsing/Shunting-yard_algorithm#Python
# http://rosettacode.org/wiki/Parsing/RPN_calculator_algorithm#Python
with open("input") as f:
    data = f.read().strip().split("\n")


def calc(s):
    a=[]
    b={'+': lambda x,y: y+x, '-': lambda x,y: y-x, '*': lambda x,y: y*x,'/': lambda x,y:y/x,'^': lambda x,y:y**x}
    for c in s.split():
        if c in b: a.append(b[c](a.pop(),a.pop()))
        else: a.append(int(c))
    return a[0]

from collections import namedtuple
from pprint import pprint as pp
 
OpInfo = namedtuple('OpInfo', 'prec assoc')
L, R = 'Left Right'.split()
 
ops = {
 '^': OpInfo(prec=4, assoc=R),
 '*': OpInfo(prec=2, assoc=L),
 '/': OpInfo(prec=3, assoc=L),
 '+': OpInfo(prec=2, assoc=L),
 '-': OpInfo(prec=2, assoc=L),
 '(': OpInfo(prec=9, assoc=L),
 ')': OpInfo(prec=0, assoc=L),
 }
 
NUM, LPAREN, RPAREN = 'NUMBER ( )'.split()
 
 
def get_input(inp = None):
    'Inputs an expression and returns list of (TOKENTYPE, tokenvalue)'
 
    if inp is None:
        inp = input('expression: ')
    tokens = inp.strip().split()
    tokenvals = []
    for token in tokens:
        if token in ops:
            tokenvals.append((token, ops[token]))
        #elif token in (LPAREN, RPAREN):
        #    tokenvals.append((token, token))
        else:    
            tokenvals.append((NUM, token))
    return tokenvals
 
def shunting(tokenvals):
    outq, stack = [], []
    table = ['TOKEN,ACTION,RPN OUTPUT,OP STACK,NOTES'.split(',')]
    for token, val in tokenvals:
        note = action = ''
        if token is NUM:
            action = 'Add number to output'
            outq.append(val)
            table.append( (val, action, ' '.join(outq), ' '.join(s[0] for s in stack), note) )
        elif token in ops:
            t1, (p1, a1) = token, val
            v = t1
            note = 'Pop ops from stack to output' 
            while stack:
                t2, (p2, a2) = stack[-1]
                if (a1 == L and p1 <= p2) or (a1 == R and p1 < p2):
                    if t1 != RPAREN:
                        if t2 != LPAREN:
                            stack.pop()
                            action = '(Pop op)'
                            outq.append(t2)
                        else:    
                            break
                    else:        
                        if t2 != LPAREN:
                            stack.pop()
                            action = '(Pop op)'
                            outq.append(t2)
                        else:    
                            stack.pop()
                            action = '(Pop & discard "(")'
                            table.append( (v, action, ' '.join(outq), ' '.join(s[0] for s in stack), note) )
                            break
                    table.append( (v, action, ' '.join(outq), ' '.join(s[0] for s in stack), note) )
                    v = note = ''
                else:
                    note = ''
                    break
                note = '' 
            note = '' 
            if t1 != RPAREN:
                stack.append((token, val))
                action = 'Push op token to stack'
            else:
                action = 'Discard ")"'
            table.append( (v, action, ' '.join(outq), ' '.join(s[0] for s in stack), note) )
    note = 'Drain stack to output'
    while stack:
        v = ''
        t2, (p2, a2) = stack[-1]
        action = '(Pop op)'
        stack.pop()
        outq.append(t2)
        table.append( (v, action, ' '.join(outq), ' '.join(s[0] for s in stack), note) )
        v = note = ''
    return table
 

def rpn(s):
    s = s.replace('(', ' ( ').replace(')', ' ) ')
    rp = shunting(get_input(s))
    return rp[-1][2]


print(sum(calc(rpn(s)) for s in data))

ops = {
 '^': OpInfo(prec=4, assoc=R),
 '*': OpInfo(prec=2, assoc=L),
 '/': OpInfo(prec=3, assoc=L),
 '+': OpInfo(prec=3, assoc=L),
 '-': OpInfo(prec=2, assoc=L),
 '(': OpInfo(prec=9, assoc=L),
 ')': OpInfo(prec=0, assoc=L),
 }
print(sum(calc(rpn(s)) for s in data))

