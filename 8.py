import math

def castle(r, b):
    _list = []
    pi = math.pi
    for i in b:
        if -1 <= i/(2*r) <= 1:
            sata = 4*math.asin(i/(2*r))
            ho = r*sata
            _list.append(ho)
        else:
            return True
    return sum(_list) >= 2*r*pi




print(castle(5.0,[5.0, 5.0, 5.0]))