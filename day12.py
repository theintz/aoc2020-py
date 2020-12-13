with open("day12-input.txt") as f:
    vals = f.read().splitlines()

directions = {
    "L": ["N", "W", "S", "E", "N", "W", "S", "E"],
    "R": ["N", "E", "S", "W", "N", "E", "S", "W"]
}

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


# part 1
ship = Ship()

for v in vals:
    cmd = v[0]
    steps = int(v[1:])
    
    ship.apply_cmd(cmd, steps)

print(ship.x + ship.y)