#def student_grade(name,grade):
 #   result = "{x:>5} recieved {y}% on the exam".format(x=name,y=grade)
  #  return result

#print(student_grade("Reed",80))
#print()
#print(student_grade("Paige",95))

###########################################################################################

def is_palindrome(input_string):
    actual_input_string = input_string.lower()
    x = len(actual_input_string)
    y = x-1
    new_string = ""
    actual_reverse = ""
    reverse_string = actual_input_string[y::-1]
    reversing1 = reverse_string.split()
    print(reverse_string)
    for letter in actual_input_string:
        if letter != " ":
            new_string = new_string + letter
    print(new_string)
    for letter in reversing1:
        actual_reverse = actual_reverse + letter
    print(actual_reverse)
    if new_string == actual_reverse:
            return True
    else:
        return False

print(is_palindrome("Never Odd or Even"))

###########################################################################################

#def nametag(first_name,last_name):
#    x = last_name[0]
#    output_to_show = "{a} {x}.".format(a=first_name,x=x)
#    return output_to_show

#print(nametag("Jane","Smith"))

###########################################################################################

#def replace_ending(sentence,old,new):
#    x = len(sentence) - len(old)
#   if sentence.endswith(old):
#        new_sentence = sentence[:x] + new
#        return new_sentence
#   return sentence

#print(replace_ending("It's raining cats and cats","cats","dogs"))
#print()
#print(replace_ending("abcabc","abc","xyz"))

############################################################################################
