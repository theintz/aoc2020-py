with open("day10-input.txt") as f:
    vals = [int(v) for v in f.read().splitlines()]

# part 1
prev = 0
count1 = 0
count3 = 1
for v in sorted(vals):
    if v - prev == 1:
        count1 += 1
    elif v - prev == 3:
        count3 += 1
    else:
        exit("wrong joltage" + str(v))
    
    prev = v

print(count1, count3, count1*count3)

# part 2
# solved by counting all the possibilities, and multiply them together
# 2 important observations:
# 1. there are a number of values that always have to stay in the set: those separated by 3 jolts.
# only those in between are variable, so we only look at them in individual batches.
# 2. all batches are sizes 1 - 5, so we only have to calculate the possibilities for these sizes
# and multiply them together.
def handle_batch(i:int) -> int:
    if inter < 2:
        # nothing, all elements must be in the set
        return 1
    elif inter == 2:
        return 2
    elif inter == 3:
        return 4
    elif inter == 4:
        # one number in the middle must be present
        return 7
    else:
        exit("too high inter")

prev = 0
inter = 0
total = 1
for v in sorted(vals):
    if v - prev == 3:
        # print(f"= {inter}\n{v} ", end="")
    
        total *= handle_batch(inter)
        inter = 0
    else:
        # print(str(v) + " ", end="")
        inter += 1

    prev = v

# handle the final batch as well
total *= handle_batch(inter)
# print(f"= {inter}")

print(total)