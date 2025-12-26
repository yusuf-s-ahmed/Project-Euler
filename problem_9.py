import math

def check_abc(a: int, b: int):
    c_sq = a*a + b*b
    c = int(math.sqrt(c_sq))
    if c*c != c_sq:
        return False
    return a + b + c == 1000

def extractProduct(a: int, b: int):
    c = int(math.sqrt(a*a + b*b))
    return a * b * c

not_found = True
l, r = 1, 1

while not_found:
    if check_abc(l, r):
        print("Found:", l, r)
        print("Product:", extractProduct(l, r))
        not_found = False
    else:
        r += 1

    if r == 200:
        l += 1
        r = l
