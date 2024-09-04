import math

def isPentagonal(num):
    r = math.sqrt(24 * num + 1)
    return r % 6 == 5

for m in range(144, 10000000000):
    print(m)
    res = 2 * m * m - m
    if isPentagonal(res):
        print("result", res)
        break

    else: print("not found")