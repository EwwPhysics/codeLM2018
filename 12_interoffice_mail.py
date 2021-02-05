def solve(connections, path, sol="", sols=[]):
    start = path[0]
    end = path[1]
    sol += start
    if path in connections:
        s = sol + end
        try:
            if len(s) < len(min(sols, key=lambda x: len(x))):
                return [s]
            else:
                return sols
        except ValueError:
            return [s]
    else:
        c = filter(lambda x: x[0] == start, connections)
        c = list(c)
        for p in c:
            sols = solve(connections, p[1] + end, sol, sols=sols)
        return sols[0]


print(solve(['AB', 'BC', 'CD', 'BD'], "AD"))
