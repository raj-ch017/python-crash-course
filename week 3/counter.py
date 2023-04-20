def counter(start,stop):
    x = start
    y = stop
    if x > y:
        return_string = "Counting down: "
        for j in range(x,y-1,-1):
            if j == stop:
                return_string = return_string + str(j)
            else:
                return_string = return_string + str(j) + ","
            j += 1
    elif y > x:
        return_string = "Counting up: "
        for j in range(x,y+1):
            if j == stop:
                return_string = return_string + str(j)
            else:
                return_string = return_string + str(j) + ","
            j += 1
    else:
        return_string = "Counting up: "
        return_string = return_string + str(x)
    return return_string

print(counter(5,5))
print(counter(1,10))
print(counter(10,1))
    
