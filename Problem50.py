def calculateSelfPower(n):
    return n ** n

def solution(limit):
    sum = 0
    for i in range(1, limit):
        power = calculateSelfPower(i)
        sum += power
    rmd = sum % 10000000000
    return rmd

print(solution(1000))