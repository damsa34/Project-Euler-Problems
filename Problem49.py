import math
def isPrime(num):
    if num <= 1: return False
    for i in range(2, num // 2):
        if num % i == 0: return False
    return True

def calculateSum(num):
    sum = 0
    while num != 0:
        rmd = num % 10
        sum += rmd
        num //= 10
    return sum

def getNums(num):
    array = []
    while num != 0:
        rmd = num % 10
        array.append(rmd)
        num //= 10
    return array

def getSize(num):
    size = 0
    while num != 0:
        size += 1
        num //= 10
    return size

primes = []
for i in range(1009 , 9974):
    if isPrime(i): primes.append(i)

for prime in primes:
    secondPrime = prime + 3330
    thirdPrime = secondPrime + 3330
    if secondPrime in primes and thirdPrime in primes:
        firstNums = getNums(prime)
        secondNums = getNums(secondPrime)
        thirdNums = getNums(thirdPrime)
        counter = 0
        for num in firstNums:
            if num in secondNums and num in thirdNums: counter += 1
        if counter == getSize(prime):
            print("12-digit number:", prime, secondPrime, thirdPrime)       