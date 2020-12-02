def solve(code, key, complement):
    x = [int(x) for x in str(code)]
    y = [int(x) for x in str(complement)]
    for i, a in enumerate(x):
        if a + key >= 10:
            y[i] = (y[i] + 10)
        if abs(a - y[i]) > key:
            return False
    return True
