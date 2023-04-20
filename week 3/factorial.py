def factorial(n):
    result = 1
    j = n
    in1 = n + 1
    if j != 0:
        for x in range(1,in1):
            result = result * x
        return result   
    else:
        return result


a = factorial(5)
print(a)
