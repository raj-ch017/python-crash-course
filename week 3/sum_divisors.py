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
