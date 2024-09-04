def diagonal_sum(spiral_size):
    total_sum = 1 
    current_number = 1
    
    for layer in range(3, spiral_size + 1, 2):
        step = layer - 1
        for _ in range(4):
            current_number += step
            total_sum += current_number
    
    return total_sum

spiral_size = 1001
result = diagonal_sum(spiral_size)
print(result)