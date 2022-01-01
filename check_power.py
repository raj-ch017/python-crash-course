def is_power_of(number,base):
    if number < base and number != 1:
        return bool(0)  #converts value to boolean type
    num1 = number / base
    if num1 == 1 or number == 1:
        return bool(1)
    return is_power_of(num1,base)

print(is_power_of(10,2))
print(is_power_of(8,2))
    