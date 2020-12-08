import re
import itertools

with open("day7-input.txt") as f:
    rules = f.read().strip().splitlines()

regex = re.compile(r"(\w+ \w+) bags contain ((?:\d \w+ \w+ bags?[.,] ?)+|no other bag.)")

# part 1
def walk_tree(v:str) -> set:
    if v not in tree:
        return []
    
    values = tree[v]
    res = [walk_tree(r) for r in values]
    res = [item for r in res for item in r]
    
    return set(res + values)

# build a reverse tree, ie. 'key' held by 'value'
tree = {}
for r in rules:
    holder, contents = re.match(regex, r).groups()
    contents = contents.strip(".").split(",")
    contents = [" ".join(c.strip().split(" ")[1:-1]) for c in contents]
    
    for c in contents:
        if not c in tree:
            tree[c] = []
        
        tree[c].append(holder)

print(len(walk_tree("shiny gold")))

# part 2
def walk_tree_2(v:str) -> int:
    if v not in tree:
        return 0

    values = tree[v]
    count = sum([int(i[1]) for i in values])
    res = sum([walk_tree_2(i[0]) * int(i[1]) for i in values])
    
    return count + res

# here we build a forward tree, ie. 'key' holds 'value'
tree = {}
for r in rules:
    holder, contents = re.match(regex, r).groups()
    
    if contents == "no other bags":
        continue

    contents = contents.strip(".").split(",")
    
    for c in contents:
        words = c.strip().split(" ")[:-1]
        count = words[0]
        color = " ".join(words[1:])

        if not holder in tree:
            tree[holder] = []
        
        tree[holder].append((color, count))


print(walk_tree_2("shiny gold"))
