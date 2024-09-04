import math
proper = [
  0, 
  len("one"),
  len("two"),
  len("three"),
  len("four"),
  len("five"),
  len("six"),
  len("seven"),
  len("eight"),
  len("nine"),
  len("ten"),
  len("eleven"),
  len("twelve"),
  len("thirteen"),
  len("fourteen"),
  len("fifteen"),
  len("sixteen"),
  len("seventeen"),
  len("eighteen"),
  len("nineteen")]

tenth = [
  len("twenty"),
  len("thirty"),
  len("forty"),
  len("fifty"),
  len("sixty"),
  len("seventy"),
  len("eighty"),
  len("ninety")]

def below100(n):
    if n < 20: return proper[n]
    return tenth[n // 10 - 2 or 0] + proper[n % 10]

def numberLength(n):
    if n < 100: return below100(n)
    res = 0
    h = math.floor(n / 100) % 10
    t = math.floor(n / 1000)
    s = n % 100
    if n > 999: res += below100(t) + len("thousand")
    if h != 0: res += proper[h] + len("hundred")
    if s != 0: res += len("and") + below100(s)
    return res

num = 0
for i in range(1, 1001):
    num += numberLength(i)
print(num)