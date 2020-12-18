with open("day16-input.txt") as f:
    data = f.read().split("\n\n")
    defs_raw = data[0].splitlines()
    yt = [int(x) for x in data[1].splitlines()[1].split(",")]
    nts = [[int(x) for x in l.split(",")] for l in data[2].splitlines()[1:]]

defs = {}
for d in defs_raw:
    t = d.split(": ")
    did = t[0]
    drules = [tuple(r.split("-")) for r in t[1].split(" or ")]
    defs[did] = drules

print(defs, yt, nts)

# part 1
def find_in_rules(rs:dict, v:int) -> str:
    for rid, rules in rs.items():
        for min, max in rules:
            if v in range(int(min), int(max) + 1):
                return rid
    
    return None

er = 0
for t in nts:
    for ti in t:
        if not find_in_rules(defs, ti):
            er += ti
            # print(f"invalid {ti} in {t}")

print(er)

