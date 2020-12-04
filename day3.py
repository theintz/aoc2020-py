import math

with open("day3-input.txt") as f:
    values = f.read().splitlines()

def iter_trees(r:int, d:int = 1) -> list:
    i = 0
    trees = 0
    even = False

    for line in values:
        even = not even

        # skip every other line
        if d == 2 and not even:
            continue

        loc = (i * r) % 31
        trees += 1 if line[loc] == "#" else 0
        #print(line[:loc] + "X" + line[loc + 1:] + " " + str(trees))

        i += 1
    
    return trees


# part 1
print(iter_trees(3))

# part 2
res = math.prod([iter_trees(v) for v in [1, 3, 5, 7]]) * iter_trees(1, 2) 
print(res)