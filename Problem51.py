import itertools
import math

# Helper function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    
    if n <= 3:
        return True
    
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

# Function to generate all masks(0 or 1) for a given length
def generate_masks(length):
    masks = []

    for r in range(1, length):
        for positions in itertools.combinations(range(length), r):
            mask = ['0'] * length
            
            for pos in positions:
                mask[pos] = '1'

            masks.append(''.join(mask))

    return masks

# Function to replace digits in the number based on the mask
def apply_mask(number_str, mask, digit):
    result = []
    for i in range(len(mask)):
        if mask[i] == '1':
            result.append(digit)
        else:
            result.append(number_str[i])

    return ''.join(result)

def find_smallest_prime():
    number = 1
    while True:
        print(number)
        number_str = str(number)
        length = len(number_str)
        masks = generate_masks(length)

        for mask in masks:
            prime_count = 0
            smallest_prime = None

            for replacement_digit in '0123456789':
                if mask[0] == '1' and replacement_digit == '0':
                    continue

                new_number = int(apply_mask(number_str, mask, replacement_digit))

                if is_prime(new_number):
                    prime_count += 1
                    if smallest_prime is None:
                        smallest_prime = new_number

            if prime_count == 8:
                return smallest_prime
            
        number += 1

print("Smallest prime of the eight prime family: ", find_smallest_prime())