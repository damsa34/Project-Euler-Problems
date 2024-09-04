def isPandigital(num):
    trueArray = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    numArray = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while num > 0:
        rmd = num % 10
        if numArray.__contains__(rmd) and trueArray[rmd - 1] == 0:
            trueArray[rmd - 1] = 1
        num //= 10
    for i in range(len(trueArray)):
        if trueArray[i] == False: return False
    return True

def solution():
    _sum = 0
    for product in range(1234, 9877):
        print("pr", product, "sum", _sum)
        for multiplier in range(1, product // 2 + 1):
            multiplicand = product // multiplier
            if multiplicand * multiplier == product:                
                if isPandigital(int(str(product) + str(multiplicand) + str(multiplier))): 
                    _sum += product
                    break
    return _sum

print(solution())
