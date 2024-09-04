def getSolutions(p):
    count = 0
    for a in range(1, p // 2 + 1):
        for b in range(a, p // 2 + 1):
            c = p - a - b
            if a ** 2 + b ** 2 == c ** 2: count += 1
    return count

maxSolutions = 0
maxP = 0
for p in range(1, 1001):
    solutions = getSolutions(p)
    if solutions >maxSolutions:
        maxSolutions = solutions
        maxP = p

print(f"The value of p with the maximum number of solutions is {maxP} with {maxSolutions} solutions.")