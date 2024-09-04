def isPentagonal(n):
    return True if (1 + 24 * n) % 6 == 0 else False

flag = True
i = 1

while flag:
    for j in range(1, 100000000):
        print(j)
        a = i * (3 * i - 1) // 2
        b = j * (3 * j - 1) // 2
        if isPentagonal(a + b) and isPentagonal(a - b):
            print (a - b)
            flag = False
            break
    i += 1