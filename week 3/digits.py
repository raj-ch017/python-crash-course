def digits(n):
    count = 0
    if n <= 9:
        count = 1
    if n > 9:
        while (n > 0):
         n = n // 10
         count = count + 1
    return count

print(digits(25))
print(digits(144))
print(digits(10000))
print(digits(0))
