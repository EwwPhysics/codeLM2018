from collections import Counter


def s(products):
    counts = Counter(products).most_common()
    mx = counts[0][1]
    test = filter(lambda x: x[1] == mx, counts)
    return [item[0] for item in test]
