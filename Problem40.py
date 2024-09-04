def find_expression_value():
    fraction = ""
    number = 1
    target_indices = [1, 10, 100, 1000, 10000, 100000, 1000000]
    product = 1
    current_length = 0

    while current_length < 1000000:
        fraction += str(number)
        current_length += len(str(number))
        number += 1

    for index in target_indices:
        digit = int(fraction[index - 1])
        product *= digit
        print(f"Digit at position {index}: {digit}")

    return product

result = find_expression_value()
print("Result of the expression: ", result)