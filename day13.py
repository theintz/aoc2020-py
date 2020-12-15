with open("day13-input.txt") as f:
    data = f.read().splitlines()
    ts = int(data[0])
    buses = [int(x) for x in data[1].split(",") if x != "x"]

# part 1
min_diff = 1000
min_bus = 0
for b in buses:
    diff = ((ts // b + 1) * b) - ts
    
    if diff < min_diff:
        min_bus = b
        min_diff = diff

print(min_bus, min_diff, min_bus*min_diff)