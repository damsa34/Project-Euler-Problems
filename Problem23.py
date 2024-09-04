def isAbundant(n):
    properDivisors = generateProperDivisors(n)
    return sum(properDivisors) > n

def generateProperDivisors(n):
    arr = []
    for i in range(1, n):
        if n % i == 0: arr.append(i)
    return arr

def generateAbundantNumberList(limit):
    arr = []
    for i in range(1, limit + 1):   
        if isAbundant(i): 
            print(i)
            arr.append(i)
    return arr

def canBeSumOfAbundantNumbers(n, arr):
    for abundant in arr:
        if abundant >= n: break
        if n - abundant in arr: return True
    return False

arr = generateAbundantNumberList(28123)
total = 0

for n in range(1, 28124):
    print(n)
    if not canBeSumOfAbundantNumbers(n, arr): total += n
print(total)