def solve(code, description, timestamp):
    output = 1
    if (timestamp < 400 and code >= 4000) or (timestamp > 1800 and 1000 <= code <= 3000):
        output = 2
    if 5000 <= code <= 9000:
        output = 3
    if description == 'Servers melting down!':
        output = 3
    if code > 9000:
        output = 4
    if description == 'David Vonderheide was here.':
        output = 4
    return output
