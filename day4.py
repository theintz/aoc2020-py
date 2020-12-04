import re
from functools import reduce

rules = {
        "byr": r"^\d{4}$",
        "iyr": r"^\d{4}$",
        "eyr": r"^\d{4}$",
        "hgt": r"^\d{2,3}(cm|in)$",
        "hcl": r"^#[0-9a-f]{6}$",
        "ecl": r"^(amb|blu|brn|gry|grn|hzl|oth)$",
        "pid": r"^\d{9}$"
    }

def check_line(l:dict, apply_rules:bool = False) -> bool:
    # check all required fields are present
    if not all(rf in l for rf in rules.keys()):
        return False
    
    # check all the rules apply
    if apply_rules:
        if not all(re.match(rule, l[key]) for key, rule in rules.items()):
            return False
        
        if not 1920 <= int(l["byr"]) <= 2002:
            return False
        
        if not 2010 <= int(l["iyr"]) <= 2020:
            return False

        if not 2020 <= int(l["eyr"]) <= 2030:
            return False
        
        hgt_value, hgt_unit = re.match(r"^(\d{2,3})(cm|in)$", l["hgt"]).groups()

        if hgt_unit == "cm" and not 150 <= int(hgt_value) <= 193:
            return False
        
        if hgt_unit == "in" and not 59 <= int(hgt_value) <= 76:
            return False

    return True

with open("day4-input.txt") as f:
    values = f.read().split("\n\n")
    values = [re.split(r"[\s:]", v.strip()) for v in values]
    # assemble into dicts
    values = [dict(zip(v[0::2], v[1::2])) for v in values]

# part 1
res = reduce(lambda x, y: int(x) + int(y), [check_line(v) for v in values], 0)
print(res)

# part 2
res = reduce(lambda x, y: int(x) + int(y), [check_line(v, True) for v in values], 0)
print(res)