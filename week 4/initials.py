def initials(phrase):
    x = phrase.upper()  #converts the input argument to upper case
    words = x.split()   #splits the name into first name and last name
    result = ""
    for word in words:
        result = result + word[0]   #picks the first character from first name and last name
    return result

print(initials("Ratnopriya Chatterjee"))
print(initials("Rajdeep Chakraborty"))
print(initials("Aman Tiger Jaiswal"))
