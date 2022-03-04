def your_cal(opt,x,y):
    if opt <= 0 or opt >2:
        show_screen = "You have entered an invalid option."
        return show_screen
    elif opt == 1:
        #print("You have opted for sum.")
        ans = x + y
        #print("The sum is: " + str(ans))
        return ans
    elif opt == 2:
        #print("You have opted for product.")
        ans = x * y
        #print("The product is: " + str(ans))
        return ans

reply = your_cal(0,3,7)
print(reply)