"""
Complete the is_power_of function return whether the number is a power of the given base.
"""

def is_power_of(number, base):
  
  if number < base and number !=1:
   
    return bool(0)

  
  num1 = number / base
  if num1 == 1 or number == 1:
    return bool(1)
  return is_power_of(num1, base)

print(is_power_of(1,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False
