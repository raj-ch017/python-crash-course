def verify(number) : # do not change this line!

  nums = list(number)
  if int(nums[0]) == 4:
    x = 1
  else:
    return False
  v1 = int(nums[3])
  v2 = int(nums[5])
  if v1 == (v2+1):
    x = x + 1
  else:
    return False
  b = nums.copy()
  b.pop(4)
  b.pop(8)
  add = 0
  for vals in b:
    add = add + int(vals)
  if add % 4 == 0:
    x = x + 1
  else:
    return False
  n1 = int(b[0])
  n2 = int(b[1])
  num1 = (n1*10)+n2
  n3 = int(b[6])
  n4 = int(b[7])
  num2 = (n3*10)+n4
  if (num1 + num2) == 100:
    x = x + 1
  else:
    return False
  if x == 4:
    return True


input = "4094-3460-2754" # change this as you test your function
output = verify(input) # invoke the method using a test input
print(output) # prints the output of the function
# do not remove this line!
