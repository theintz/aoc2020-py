with open("day12-input.txt") as f:
    vals = f.read().splitlines()

directions = {
    "L": ["N", "W", "S", "E", "N", "W", "S", "E"],
    "R": ["N", "E", "S", "W", "N", "E", "S", "W"]
}

# part 1
class Ship:
    x: int = 0
    y: int = 0
    b: str = "E"

    def move(self, steps:int, dir:str = "") -> None:
        if dir == "":
            dir = self.b
        
        if dir == "N":
            self.y -= steps
        elif dir == "E":
            self.x += steps
        elif dir == "S":
            self.y += steps
        elif dir == "W":
            self.x -= steps
        else:
            exit("unknown dir " + dir)
    
    def turn(self, dir:str, turns:int = 1) -> None:
        if dir != "L" and dir != "R":
            exit("unknown dir " + dir)

        index = directions[dir].index(self.b)
        self.b = directions[dir][index + turns]
    
    def apply_cmd(self, cmd:str, steps:int) -> None:
        if cmd == "F":
            self.move(steps)
        elif cmd in ["N", "E", "S", "W"]:
            self.move(steps, cmd)
        elif cmd in ["L", "R"]:
            self.turn(cmd, int(steps / 90))
        else:
            exit("unknown cmd " + cmd)


ship = Ship()

for v in vals:
    ship.apply_cmd(v[0], int(v[1:]))

print(abs(ship.x + ship.y))

# part 2
class Ship2(Ship):
    way_x = 10
    way_y = -1

    def move_to_way(self, steps:int) -> None:
        self.x += self.way_x * steps
        self.y += self.way_y * steps

    def move_way(self, dir:str, steps:int) -> None:
        if dir == "N":
            self.way_y -= steps
        elif dir == "E":
            self.way_x += steps
        elif dir == "S":
            self.way_y += steps
        elif dir == "W":
            self.way_x -= steps
        else:
            exit("unknown dir " + dir)
    
    def rot_way(self, dir:str, steps:int) -> None:
        # probably a nicer way here, but it's late
        old_x = self.way_x
        old_y = self.way_y

        if (dir == "R" and steps == 1) or (dir == "L" and steps == 3):
            self.way_x = -old_y
            self.way_y = old_x
        elif (dir == "R" and steps == 2) or (dir == "L" and steps == 2):
            self.way_x = -old_x
            self.way_y = -old_y
        elif (dir == "R" and steps == 3) or (dir == "L" and steps == 1):
            self.way_x = old_y
            self.way_y = -old_x
        else:
            exit("unknown combination")

    def apply_cmd2(self, cmd:str, steps:int) -> None:
        if cmd == "F":
            self.move_to_way(steps)
        elif cmd in ["N", "E", "S", "W"]:
            self.move_way(cmd, steps)
        elif cmd in ["L", "R"]:
            self.rot_way(cmd, int(steps / 90))
        else:
            exit("unknown cmd " + cmd)

ship = Ship2()

for v in vals:
    ship.apply_cmd2(v[0], int(v[1:]))

print(abs(ship.x + ship.y))