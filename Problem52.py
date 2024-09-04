def has_same_digits(x):
    sorted_x = sorted(str(x))
    for multiple in range(2, 7):
        if sorted(str(x * multiple)) != sorted_x:
            return False
    return True

def find_smallest_integer():
    x = 1
    while True:
        print("x: ", x)
        if has_same_digits(x):
            return x
        x += 1

print(find_smallest_integer())