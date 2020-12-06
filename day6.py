with open("day6-input.txt") as f:
    groups = f.read().split("\n\n")
    groups = [g.splitlines() for g in groups]

# part 1
sum = 0    
for g in groups:
    checks = {}

    for line in g:
        for sel in line:
            checks[sel] = True
    
    sum += len(checks)

print(sum)

# part 2
sum = 0    
for g in groups:
    checks = {}

    for line in g:
        for sel in line:
            if sel not in checks:
                checks[sel] = 0
            
            checks[sel] += 1

    for c, cnt in checks.items():
        if cnt == len(g):
            sum += 1

print(sum)