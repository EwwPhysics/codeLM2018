from collections import Counter


def s(products):
    counts = Counter(products).most_common()
    mx = counts[0][1]
    max_products = [product[0] for product in filter(lambda x: x[1] == mx, counts)]
    return max_products
