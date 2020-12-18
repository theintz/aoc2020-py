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
def find_in_rules(rs:dict, v:int) -> list:
    ret = []
    for rid, rules in rs.items():
        for min, max in rules:
            if v in range(int(min), int(max) + 1):
                ret.append(rid)
    
    return ret

er = 0
for t in nts:
    for ti in t:
        if not find_in_rules(defs, ti):
            er += ti
            # print(f"invalid {ti} in {t}")

print(er)

# part 2
# first remove the invalid ones
valid_nts = []
for t in nts:
    valid = True
    for ti in t:
        if not find_in_rules(defs, ti):
            valid = False
    
    if valid:
        valid_nts.append(t)

removed = len(nts) - len(valid_nts)
print(f"removed {removed} nts entries")

# then go column by column and find all matching rules
tmp_mapping = {}
for idx in range(len(valid_nts[0])):
    idx_rls = set(defs.keys())
    for col in [x[idx] for x in valid_nts]:
        idx_rls.intersection_update(find_in_rules(defs, col))
    tmp_mapping[idx] = idx_rls
    
print(tmp_mapping)

# finally solve the rules by iterating
mapping = {}
while len(tmp_mapping) > 0:
    # first find items with only one rule and add them to the final mapping
    for idx, rl in [(idx, rls.pop()) for idx, rls in tmp_mapping.items() if len(rls) == 1]:
        mapping[rl] = idx
        tmp_mapping.pop(idx)
    
    # then update rules for all remaining items
    for idx, rls in tmp_mapping.items():
        rls.difference_update(mapping.keys())

print(mapping)

# last step: apply to our ticket
prod = 1
for idx in [idx for col, idx in mapping.items() if col.startswith("departure")]:
    prod *= yt[idx]

print(prod)
