from itertools import permutations

def lexicographicPermutations(n):
    n_str = str(n)
    permutations_list = [int(''.join(perm)) for perm in permutations(n_str)]
    permutations_list.sort()
    return permutations_list

permList = lexicographicPermutations(1234567890)
print(len(permList))
if len(permList) >= 1000000: 
    print("got ", permList[999999])
    