import re

with open('input') as f:
    text = f.read()

while '\n\n\n' in text:
    text = text.replace('\n\n\n', '\n\n')
passports = text.split('\n\n')
passports = [dict(kv.split(':') for kv in p.replace('\n\n', ' ').split()) for p in passports]
valid = { 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', }
print(sum(1 for p in passports if valid.issubset(p.keys())))

from functools import partial
def int_val(least, most, n):
    return least<=int(n)<=most
v_byr = partial(int_val, 1920, 2002)
v_iyr = partial(int_val, 2010, 2020)
v_eyr = partial(int_val, 2020, 2030)
v_cm = partial(int_val, 150, 193)
v_in = partial(int_val, 59, 76)

class NotValid(Exception):
    pass

def has_correct_keys(passport):
    if not valid.issubset(passport.keys()):
        raise NotValid("keys")
def valid_field(key, func, passport):
    if not func(passport[key]):
        raise NotValid(key)
def valid_ecl(passport):
    if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth",]:
        raise NotValid("ecl")
def valid_pid(passport):
    if not re.match(r"^\d{9}$", passport["pid"]):
        raise NotValid("pid")
def valid_hcl(passport):
    if not re.match(r"^\#[0-9a-f]{6}$", passport["hcl"]):
        raise NotValid("hcl")
def valid_hgt(passport):
    if not (m := re.match(r"^(\d+)(cm|in)$", passport["hgt"])):
        raise NotValid
    if m.group(2)=="in":
        if not v_in(m.group(1)):
            raise NotValid
    else:
        if not v_cm(m.group(1)):
            raise NotValid
    
checks = [has_correct_keys, 
        partial(valid_field, "byr", v_byr),
        partial(valid_field, "iyr", v_iyr),
        partial(valid_field, "eyr", v_eyr),
        valid_ecl,
        valid_pid,
        valid_hcl,
        valid_hgt,
        ]
def is_valid(passport):
    try:
        for check in checks:
            check(passport)
        return True
    except NotValid as e:
        return False

print(len(list(filter(is_valid, passports))))
