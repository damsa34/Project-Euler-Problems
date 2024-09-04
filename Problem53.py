from math import factorial

# My solution
def return_combination_value(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

def count():
    counter = 0
    for n in range(1, 101):
        print("n: ", n)
        for r in range(1, n):
            if return_combination_value(n, r) > 1000000:
                counter += 1

    return counter

# print(count())

# ChatGPT optimized solution
def count_combinations_exceeding_million():
    counter = 0
    limit = 1000000

    for n in range(1, 101):
        print("n: ", n)
        combination = 1

        for r in range(1, n // 2 + 1):
            combination = combination * (n - r + 1) // r

            if combination > limit:
                counter += n - 2 * r + 1
                break

    return counter

print(count_combinations_exceeding_million())