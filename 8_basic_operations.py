def solve(str):
    nums = [int(x) for x in str]
    binary = '0'*len(str)
    while binary != bin(int('1'*len(str), 2) + 1)[2:]:
        test = [-x if binary[i] == '1' else x for i, x in enumerate(nums)]
        if sum(test) == 0:
            return True
        binary = bin(int(binary, 2) + 1)[2:].rjust(len(str), '0')
    return False
