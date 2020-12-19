# I know there are prettier ways to achieve this, for example encapsulate the functionality
# in classes, but I don't have time for that now, so here's an almost identical copy of the
# first part with an additional parameter added. Sorry Uncle Bob.

with open("day17-input.txt") as f:
    input = f.read()

# input = ".#.\n..#\n###"

# part 1
s = {}

def set_point(space:dict, x:int, y:int, z:int, w:int, val:str) -> None:
    space[f"x{x};y{y};z{z};w{w}"] = val

def get_point(space:dict, x:int, y:int, z:int, w:int) -> str:
    key = f"x{x};y{y};z{z};w{w}"
    return space[key] if key in space else None

adjacency = [(i, j, k, l) for i in (-1, 0, 1) 
    for j in (-1, 0, 1) for k in (-1, 0, 1) 
    for l in (-1, 0, 1) if not (i == j == k == l == 0)]
def neighbors(space:dict, x:int, y:int, z:int, w:int) -> list:
    for dx, dy, dz, dw in adjacency:
        point = get_point(space, x + dx, y + dy, z + dz, w + dw)
        
        if not point:
            continue
        
        yield point

def state_neighbors(space:dict, x:int, y:int, z:int, w:int) -> int:
    return sum([1 if s == "#" else 0 for s in neighbors(space, x, y, z, w)])

def max_dim(space:dict, dim:str) -> (int, int):
    mi = ma = 0
    for v in [v for sl in [x.split(";") for x in space.keys()] for v in sl if v.startswith(dim)]:
        mi = min(mi, int(v[1:]))
        ma = max(ma, int(v[1:]))
    
    return (mi, ma)

z = w = 0
for y, l in enumerate(input.splitlines()):
    for x, v in enumerate(l):
        set_point(s, x, y, z, w, v)

print(s)
print("This will take a while...")

cycles = [s]
for cycle in range(6):
    prev_s = cycles[-1]
    sn = {}

    min_x, max_x = max_dim(prev_s, "x")
    min_y, max_y = max_dim(prev_s, "y")
    min_z, max_z = max_dim(prev_s, "z")
    min_w, max_w = max_dim(prev_s, "w")
    dims = [(x, y, z, w) for x in range(min_x - 1, max_x + 2) 
        for y in range(min_y - 1, max_y + 2) 
        for z in range(min_z - 1, max_z + 2) 
        for w in range(min_w - 1, max_w + 2)]

    for x, y, z, w in dims:
        p = get_point(prev_s, x, y, z, w) or "."
        nb = neighbors(prev_s, x, y, z, w)
        st = state_neighbors(prev_s, x, y, z, w)
        
        # we explicitly list every case here
        nv = ""
        if p == "#":
            nv = "#" if st in range(2, 4) else "."
        elif p == ".":
            nv = "#" if st == 3 else "."
        else:
            continue
        
        # print(x, y, z, p, list(nb), st, nv)
        set_point(sn, x, y, z, w, nv)
    
    cycles.append(sn)
    # print(sn)

print(sum([1 if s == "#" else 0 for s in cycles[-1].values()]))