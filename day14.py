import re

with open("day14-input.txt") as f:
    data = f.read().splitlines()


def set_mask(m:str) -> tuple:
    mask0 = int(m.replace("X", "1"), 2)
    mask1 = int(m.replace("X", "0"), 2)

    return (mask0, mask1)

def apply_mask(v:int, masks:tuple) -> int:
    return (v & masks[0]) | masks[1]

mem = {}
masks = ()
for l in data:
    if l.startswith("mask"):
        # update the masks
        masks = set_mask(l[7:])
        # print(masks)
    elif l.startswith("mem"):
        # apply the masks
        loc, val = re.match(r"^mem\[(\d+)\] = (\d+)$", l).groups()
        # print(loc, val)
        val = apply_mask(int(val), masks)
        # print(val)
        mem[int(loc)] = val
    else:
        exit("unknown instruction")

print(sum(mem.values()))