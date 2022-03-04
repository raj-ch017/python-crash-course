def check_format(number) : # do not change this line!

  num = list(number)
  a = len(num)
  if a > 14 or a < 14:
    return False
  b = ['0','1','2','3','4','5','6','7','8','9']
  for i in range(0,14):
    if i!= 4 and i != 9:
      if num[i] not in b:
        return False
    if i == 4 or i == 9:
      if num[i] != '-':
        return False

  

input = "1234-555506646"
output = check_format(input) # invoke the method using a test input
print(output) # prints the output of the function
# do not remove this line!
