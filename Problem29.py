def generateArray():
    arr = []
    for a in range(2, 101):
        for b in range(2, 101):
            power = a ** b
            if arr.__contains__(power) != True:
                arr.append(power)
    return arr

arr = generateArray()
print(len(arr))