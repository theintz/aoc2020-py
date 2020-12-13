with open("day11-input2.txt") as f:
    seats = [[char for char in l] for l in f.read().splitlines()]

max_x = len(seats[0]) - 1
max_y = len(seats) - 1

# blatantly copied from https://stackoverflow.com/questions/2373306/pythonic-and-efficient-way-of-finding-adjacent-cells-in-grid
adjacency = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if not (i == j == 0)]

def adj_seats(x:int, y:int, seats:list) -> list:
     for dx, dy in adjacency:
          if 0 <= x + dx <= max_x and 0 <= y + dy <= max_y:
              yield seats[y + dy][x + dx]

def num_adj_occ(x:int, y:int, seats:list) -> int:
    return sum([1 if s == "#" else 0 for s in adj_seats(x, y, seats)])

def iter_seats(seats:list, seat_counter = num_adj_occ, thres_vis: int = 4) -> list:
    n_seats = []
    y = 0
    for line in seats:
        n_line = []
        x = 0
        
        for seat in line:
            cnt = seat_counter(x, y, seats)
            
            if seat == ".":
                v = "."
            elif seat == "L" and cnt == 0:
                v = "#"
            elif seat == "#" and cnt >= thres_vis:
                v = "L"
            else:
                v = seat
            
            n_line.append(v)
            x +=1
        
        n_seats.append(n_line)
        y += 1
    
    return n_seats

def cmp_seats(a:list, b:list) -> bool:
    for l_a, l_b in zip(a, b):
        for s_a, s_b in zip(l_a, l_b):
            if s_a != s_b:
                return False
    
    return True

def print_seats(seats:list) -> None:
    for l in seats:
        for s in l:
            print(s, end="")
        print()
    print("\n")


# part 1
# print_seats(seats)
# prev_iter = seats
# while True:
#     cur_iter = iter_seats(prev_iter.copy())
#     # print_seats(cur_iter)

#     if cmp_seats(cur_iter, prev_iter):
#         cnt = sum([sum([1 if s == "#" else 0 for s in l]) for l in cur_iter])
#         print(cnt)
#         break

#     prev_iter = cur_iter

# part 2
def adj(x:int, y:int, dir:str) -> list:
    # returns a list of tuples with all possible adjacency indices for a given direction
    if dir == "W":
        while x > 0:
            x -= 1
            yield (x, y)
    elif dir == "N":
        while y > 0:
            y -= 1
            yield (x, y)
    elif dir == "E":
        while x < max_x:
            x += 1
            yield (x, y)
    elif dir == "S":
        while y < max_y:
            y += 1
            yield (x, y)
    elif dir == "NW":
        while x > 0:
            x -= 1
            yield from adj(x, y, "N")
    elif dir == "NE":
        while x < max_x:
            x += 1
            yield from adj(x, y, "N")
    elif dir == "SE":
        while x < max_x:
            x += 1
            yield from adj(x, y, "S")
    elif dir == "SW":
        while x > 0:
            x -= 1
            yield from adj(x, y, "S")
    else:
        exit("wrong dir")

dirs = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
def adj_seats2(x:int, y:int, seats:list) -> list:
    # here we apply the special rules where "adjacency" skips empty seats
    for dir in dirs:
        for nx, ny in adj(x, y, dir):
            if seats[ny][nx] != ".":
                print(dir, nx, ny)
                yield seats[ny][nx]
                break

def num_adj_occ2(x:int, y:int, seats:list) -> int:
    return sum([1 if s == "#" else 0 for s in adj_seats2(x, y, seats)])

print_seats(seats)
prev_iter = seats
while True:
    cur_iter = iter_seats(prev_iter.copy(), seat_counter=num_adj_occ2, thres_vis=5)
    print_seats(cur_iter)

    if cmp_seats(cur_iter, prev_iter):
        cnt = sum([sum([1 if s == "#" else 0 for s in l]) for l in cur_iter])
        print(cnt)
        break

    prev_iter = cur_iter
