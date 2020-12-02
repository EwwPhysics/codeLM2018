def email(name):
    name = name.lower()
    a = name.split()
    if len(a[-1]) > 5:
        a[-1] = a[-1][:5]
    if len(a) == 3:
        return a[0][0] + a[1][0] + a[2] + '@NewWaveComputers.com'
    else:
        return a[0][0] +  a[1] + '@NewWaveComputers.com'
