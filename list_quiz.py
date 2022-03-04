#quiz1

#def change_filename(filenames):
#    x = 0
#    to_check = '.hpp'
#    newfilenames = []
#    for file in filenames:
#        if to_check in file:
#            x = file.split(".")
#            y = x[0] + ".h"
#            newfilenames.append(y)
#        else:
#            newfilenames.append(file)
#    return newfilenames

#print(change_filename(['program.c','stdio.hpp','this.hpp','hpp.out']))

##############################

#def pig_latin(text):
#    words = text.split(" ")
#    say = []
#    for word in words:
#        first_char = word[0]
#        word_to_add = word[1:]
#        new_word = word_to_add + first_char + "ay"
#        say.append(new_word)
#        #print(new_word)
#     saying = " ".join(say)
#   return saying

#print(pig_latin("hello how are you"))
#print(pig_latin("programming in python is fun"))

##############################

#def octal_to_string(octal):
#    octal_in_string = str(octal)
#    permission_list = []
#    x = 1
#    j = 0
#    for characters in octal_in_string:
#            if characters == '7':
#                return_statement = "rwx"
#            elif characters == '6':
#                return_statement = "rw-"
#            elif characters == '5':
#                return_statement = "r-x"
#            elif characters == '4':
#                return_statement = "r--"
#            elif characters == '3':
#                return_statement = "-wx"
#            elif characters == '2':
#                return_statement = "-w-"
#            elif characters == '1':
#                return_statement = "--x"
#            else:
#                return_statement = "---"
#            permission_list.append(return_statement)
#    #print(permission_list)
#    final_list = "".join(permission_list)
#    print(final_list)
#    print(type(final_list))

#octal_to_string(755)
#octal_to_string(644)

###############################################################

from typing import final


def group_list(group,users):
    members = users
    member_list = []
    x = len(members)
    group_stat = group + ": "
    for y in range(x):
        j = members[y]
        member_list.append(j)
    print(member_list)
    a = ", ".join(member_list)
    final_list = group_stat + a
    print(final_list)

(group_list("Engineering", ["Kim", "Jay", "Tom"]))
group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])