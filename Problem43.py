from itertools import permutations

def is_divisible(sub_string, prime):
    return int(sub_string) % prime == 0

def find_sum():
    primes = [2, 3, 5, 7, 11, 13, 17]
    pandigital_permutations = permutations('0123456789')
    total_sum = 0

    for perm in pandigital_permutations:
        print(total_sum)
        num_str = ''.join(perm)
        divisible = True
        for i in range(7):
            if not is_divisible(num_str[i + 1: i + 4], primes[i]):
                divisible = False
                break

        if divisible:
            total_sum += int(num_str)

    return total_sum

print("Final sum: ", find_sum())