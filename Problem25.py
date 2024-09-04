import math

def solution(digits):
    a, b = 1, 1
    index = 2
    while len(str(b)) < digits:
        a, b = b, a + b
        index += 1
    return index

index = solution(1000)
print(index)