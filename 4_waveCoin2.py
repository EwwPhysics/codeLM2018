def solve(num):
    x = {x for x in range(2, 9)}
    for i in x:
        div = num / i
        if div in x:
            return True
    return False
