def solve(products):
    product = {}
    for i in products:
        a = product.get(i, 0) + 1
        product[i] = a
    count = 0
    result = []
    for key, value in product.items():
        if value > count:
            result = [key]
            count = value
        elif value == count:
            result.append(key)
    return result
