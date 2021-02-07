def solve(connections, path, s="", sol=''):
    start, end = path
    s += start

    if path in connections:
        ans = s + end
        if not sol:
            return ans
        elif len(ans) < len(sol):
            return ans
        return sol

    else:
        c = list(filter(lambda x: x[0] == start, connections))
        for p in c:
            sol = solve(connections, p[1] + end, s, sol)
        return sol
