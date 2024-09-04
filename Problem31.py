def solution(target):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    table = [0] * (target + 1)
    table[0] = 1
    for i in range(len(coins)):
        for j in range(coins[i], target + 1):
            table[j] += table[j - coins[i]]
    return table[target]
print(solution(200)) 