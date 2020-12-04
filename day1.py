with open("day1-input.txt") as f:
    values = f.read().splitlines()
    values = [int(v) for v in values]

# part 1
result = [a * b for a in values for b in values if a + b == 2020]
print(result[0])

# part 2
result = [a * b * c for a in values for b in values for c in values if a + b + c == 2020]
print(result[0])