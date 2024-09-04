def is_palindrome(n):
    string_n = str(n)
    return string_n == string_n[::-1]

def base10_to_base2(n):
    return bin(n)[2:]

def solution():
    base10_numbers = []
    for i in range(1, 1000000):
        if is_palindrome(i): 
            base10_numbers.append(i)

    sum = 0
    for i in base10_numbers:
        base2_number = base10_to_base2(i)
        if is_palindrome(base2_number):
            sum += i

    return sum

print(solution())
