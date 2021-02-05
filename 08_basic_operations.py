import itertools


def s(str):
    nums = [int(x) for x in str]
    binary = itertools.product(range(2), repeat=len(str))
    for combo in binary:
        test = [-x if combo[i] == 1 else x for i, x in enumerate(nums)]
        if sum(test) == 0:
            return True
    return False
