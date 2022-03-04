def squares(n):
    return n**2

def sum_squares(x):
    input = x
    sum = 0
    for n in range(input):          # range starts from a value of 0 and runs till (input-1)
        a = squares(n)
        sum += a
        print("Loop run number: " + str(n))
    return sum


print(sum_squares(3))



