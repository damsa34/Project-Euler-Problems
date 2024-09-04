from itertools import permutations
import itertools

# My solution
def init_pandigits_array():
    digits = '123456789'    
    pandigital_permutations = permutations(digits)
    pandigital_numbers = [int(''.join(p)) for p in pandigital_permutations]
    pandigital_numbers.sort(reverse = True)
    return pandigital_numbers

def solution():
    pandigital_numbers = init_pandigits_array()
    for pandigital in pandigital_numbers:
        print(pandigital)
        str_pandigital = str(pandigital)

        for i in range(1, 10000):
            concatenated_product = ""
            n = 1
            while len(concatenated_product) < 9:
                concatenated_product += str(i * n)
                n += 1

            if concatenated_product == str_pandigital:
                return pandigital
            
    return 0

#ChatGPT Solution
def is_pandigital(number_str):
    return len(number_str) == 9 and set(number_str) == set('123456789')

def find_largest_pandigital():
    largest_pandigital = 0

    for x in range(1, 10000):
        concatenated_product = ""

        for n in range(1, 10):
            concatenated_product += str(x * n)

            if len(concatenated_product) > 9:
                break

            if len(concatenated_product) == 9 and is_pandigital(concatenated_product):
                largest_pandigital = max(largest_pandigital, int(concatenated_product))

    return largest_pandigital

print(find_largest_pandigital())