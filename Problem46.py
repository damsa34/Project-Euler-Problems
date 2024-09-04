import itertools
import math

# My solution
def return_prime_list(limit):
    if limit < 2:
        return []
    
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for number in range(2, int(limit**0.5) + 1):
        if is_prime[number]:
            for multiple in range(number * number, limit + 1, number):
                is_prime[multiple] = False

    primes = [number for number in range(limit + 1) if is_prime[number]]

    return primes

def is_composite(n):
    if n <= 1:
        return False
    if n <= 3: 
        return False
    
    if n % 2 == 0 or n % 3 == 0:
        return True
    
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return True
        
    return False

def solution():
    primes = return_prime_list(1000000)
    
    for x in itertools.count(start = 9, step = 2):
        is_sum = False
        if is_composite(x):
            for prime in primes:
                if prime >= x:
                    break

                for s in range(1, x // 2):
                    sum = prime + 2 * pow(s, 2)
                    if sum == x:
                        is_sum = True
                        break

                    elif sum > x:
                        break

            if is_sum == False:
                return x
                
    return 0

# print("Smallest odd composite: ", solution())

# ChatGPT optimized solution
# Same helper functions as in my solution

def solution2():
    limit = 10000
    primes = return_prime_list(limit)
    prime_set = set(primes)

    for x in itertools.count(start = 9, step = 2):
        if x in prime_set:
            continue

        is_sum = False
        if is_composite(x):
            for prime in primes:
                if prime >= x:
                    break

                max_s = int(math.sqrt((x - prime) / 2))
                for s in range(1, max_s + 1):
                    sum = prime + 2 * s * s
                    if sum == x:
                        is_sum = True
                        break

                    elif sum > x:
                        break

                if is_sum: break

            if not is_sum:
                return x
            
#print("Smallest odd composite: ", solution2())