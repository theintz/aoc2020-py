import re

regex = re.compile(r"^(\d{1,2})-(\d{1,2}) (\w): (\w+)$")

with open("day2-input.txt") as f:
    values = f.read().splitlines()
    values = [re.match(regex, v).groups() for v in values]

# part 1
res = [(min, max, s, s.count(c)) for (min, max, c, s) in values if s.count(c) >= int(min) and s.count(c) <= int(max)]
#print(res)
print(len(res))

# part 2
res = [s for (pos1, pos2, c, s) in values if bool(s[int(pos1) - 1] == c) ^ bool(s[int(pos2) - 1] == c)]
#print(res)
print(len(res))