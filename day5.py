with open("day5-input.txt") as f:
    vals = f.read().splitlines()

# part 1
seatids = []
highest = 0
for v in vals:
    row = int(v[:7].replace("B", "1").replace("F", "0"), 2)
    column = int(v[7:].replace("R", "1").replace("L", "0"), 2)
    seatid = row * 8 + column

    if seatid > highest:
        highest = seatid
    
    seatids.append(seatid)

print(highest)

# part 2
prev_seatid = 0
for s in sorted(seatids):
    if prev_seatid + 2 == s:
        print(s - 1)
        break
    
    prev_seatid = s