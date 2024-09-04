def isPrime(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True

def isCircularPrime(n):
    if n < 10 and isPrime(n): return True
    counter = len(str(n))
    while counter > 0:
        if not isPrime(n): return False
        rmd = n % 10
        n //= 10
        nStr = str(n)
        rmdStr = str(rmd)
        result = rmdStr + nStr
        n = int(result)
        counter -= 1
    if counter == 0: return True

sum = 0
for i in range(1, 1000000):
    if isCircularPrime(i): 
        sum += 1
        print(i, sum)
print("sum", sum)
