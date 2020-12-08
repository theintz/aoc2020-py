from copy import deepcopy

with open("day8-input.txt") as f:
    code = f.read().splitlines()
    code = [l.split() for l in code]

class ExecutionContext:
    ip = 0
    ax = 0
    status = "stopped"

    def __str__(self):
        return f"ctx {self.status} ip: {self.ip} ax: {self.ax}"

def run_i(opc:str, arg:str, ctx:ExecutionContext) -> None:
    if opc == "nop":
        return
    elif opc == "acc":
        arg = int(arg.strip("+"))
        ctx.ax += arg
        return
    elif opc == "jmp":
        arg = int(arg.strip("+"))
        # we subtract another 1 here, because it will get added again in the outer loop
        ctx.ip += arg - 1
        return
    else:
        exit("unknown opc: " + opc)

def run(code:list) -> ExecutionContext:
    ctx = ExecutionContext()
    ctx.status = "running"
    seen = []

    while True:
        if ctx.ip > len(code) - 1:
            # if the ip is larger than the code, we are done
            ctx.status = "terminated"
            break

        if ctx.ip in seen:
            # this means we have reached our termination condition
            ctx.status = "infloop"
            break
        
        line = code[ctx.ip]
        seen.append(ctx.ip)
        run_i(line[0], line[1], ctx)
        
        if ctx.status != "running":
            break
        
        ctx.ip += 1
    
    return ctx


# part 1
ctx = run(code)
print(ctx.ax)

# part 2
i = 0
while i < len(code):
    if code[i][0] == "nop" or code[i][0] == "jmp":
        copy = deepcopy(code)
        copy[i][0] = "nop" if copy[i][0] == "jmp" else "jmp"
        ctx = run(copy)

        if ctx.status == "terminated":
            print(ctx)
            break

    i += 1

