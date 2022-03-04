def sum_divisors(n):
    sum = 0
    div = 1
    input = n
    while div < input:
        if input % div == 0:
            sum = sum + div 
            div += 1
        else:
            div +=1
    return sum

#print(sum_divisors(36))  

def multiplication_table(number):
    input1 = number
    multiplier = 1
    while multiplier <= 5:
        result = input1 * multiplier
        if result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1

multiplication_table(2) 