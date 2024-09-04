from itertools import permutations

def prime(n):
    if n <= 1: return False

    if n <= 3: return True

    if n % 2 == 0 or n % 3 == 0: return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0: return False
        i += 6
    
    return True

def pandigital_prime():
    for length in range(9, 0, -1):
        digits = ''.join(str(i) for i in range(1, length + 1))
        for perm in sorted(permutations(digits), reverse=True):
            number = int(''.join(perm))
            if prime(number):
                return number
            
    return None

result = pandigital_prime()
print(result)

