import io
import re

def isTriangular(n):
    discriminant = 1 + 8 * n
    sqrt_discriminant = int(discriminant**0.5)

    return sqrt_discriminant ** 2 == discriminant

def getNameValue(name):
    letters = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7,
               'H' : 8, 'I' : 9, 'J' : 10, 'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14,
               'O' : 15, 'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20, 'U' : 21,
               'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26}
    name = name.upper()
    nameValue = sum(letters[letter] for letter in name if letter in letters)
    return nameValue

text_file = open("words.txt", "r")
data = text_file.read()
names = re.findall(r'"([^"]*)"', data) 

counter = 0

for name in names:
    
    value = getNameValue(name)
    print("name: ", name, "value: ", value)
    print(counter)
    if isTriangular(value): counter += 1

text_file.close()