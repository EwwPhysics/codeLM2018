def solve(products):
    most = 0
    product = {}
    for i in products:
        count = products.count(i)
        if count == most:
            product.add(i)
            most = count
        elif count > most:
            product = {i}
            most = count
    product = sorted(product)
    return product
