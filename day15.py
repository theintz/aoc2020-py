input = [1,2,16,19,18,0]

# part 1
def rev_index(hay:list, need:int) -> int:
    return max(loc for loc, val in enumerate(hay) if val == need)

def iter_input(l:list, iterations:int) -> None:
    while len(l) <= iterations:
        last = l[-1]
        new = len(l) - rev_index(l[:-1], last) - 1 if last in l[:-1] else 0
        l.append(new)

iter_input(input, 2019)
print(input[2019])

# part 2
input = [1,2,16,19,18,0]

def fill_indices(l:list) -> dict:
    d = {}

    # we construct a dict of values to their indices
    for i, n in enumerate(l):
        if n not in d:
            d[n] = []
        d[n].append(i)
    
    return d

def iter_input2(l:list, iterations:int) -> None:
    indices = fill_indices(l)

    while len(l) <= iterations:
        last = l[-1]
        idxs = indices[last]
        
        # this list will always have at least one element, since we put it in there in the previous run
        if len(idxs) > 1:
            new = idxs[-1] - idxs[-2]
        else:
            new = 0

        if new not in indices:
            indices[new] = [len(l)]
        else:
            # we only store the last two indices in order not to kill our RAM
            prev_idx = indices[new][-1]
            indices[new] = [prev_idx, len(l)]
        
        l.append(new)

        # if len(l) % 10000 == 0:
            # print(len(l), len(indices))

print("This will take a while...")
iter_input2(input, 29999999)
print(input[29999999])