from math import gcd
from functools import reduce

def lcm(a, b):
    return a * b // gcd(a, b)
def getTotalX(a, b):
    output = 0

    # LCM of list a
    low = reduce(lcm, a)
    # GCD of list b
    high = reduce(gcd, b)

    for i in range(low, high + 1):
        case1 = all(i % c1 == 0 for c1 in a)   # divisible by all in a
        case2 = all(c2 % i == 0 for c2 in b)   # divides all in b
        output += case1 * case2

    return output
