import itertools

with open("day9-input.txt") as f:
    vals = [int(z) for z in f.read().splitlines()]

# part 1
window = 25
i = window
match = -1
target = 0

while i < len(vals) - 1:
    w = vals[i - window:i]
    target = vals[i]
    found = False

    for c in itertools.combinations(w, 2):
        if sum(c) == target:
            found = True
            break
    
    if not found:
        print("No match for " + str(target))
        match = i
        break
    
    i += 1

# part 2
for windowsize in range(2, match):
    i = windowsize

    while i < match:
        w = vals[i - windowsize:i]

        if sum(w) == target:
            print("Found match " + str(w))
            print(min(w) + max(w))
            break
            
        i += 1