def testing_operators(x,y,c):
    if c <=0 or c > 3:
        print("Invalid option entered!")
        return 
    if c==1:
        print("You have opted for arithmetic division!")
        ans = x/y 
        return ans
    if c==2:
        print("You have opted for floor division!")
        ans = x//y
        return ans
    if c==3:
        print("You have opted for modulus!")
        ans = x%y 
        return ans

a = testing_operators(15,4,0)
print(a)
