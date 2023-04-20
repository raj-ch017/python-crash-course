def check_power(number,base):
    if number < base and number != 1:
        return bool(0)  #converts value to boolean type
    num1 = number / base
    if num1 == 1 or number == 1:
        return bool(1)
    return check_power(num1,base)

print(check_power(10,2))
print(check_power(8,2))
    
