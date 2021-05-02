import re

with open('04-input') as f:
    text = f.read()

while '\n\n\n' in text:
    text = text.replace('\n\n\n', '\n\n')
passports = text.split('\n\n')
passports = [dict(kv.split(':') for kv in p.replace('\n\n', ' ').split()) for p in passports]
valid = { 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', }
print(sum(1 for p in passports if valid.issubset(p.keys())))

from functools import partial
def int_val(least, most, n):
    return least<=n<=most
v_byr = partial(int_val, 1920, 2002)
v_iyr = partial(int_val, 2010, 2020)
v_eyr = partial(int_val, 2020, 2030)
v_cm = partial(int_val, 150, 193)
v_in = partial(int_val, 59, 76)

def is_valid(passport):
    valid.issubset(p.keys())
