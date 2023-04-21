#def get_word(sentence,n):
#    if n > 0:
#        words = sentence.split()
#        if n <= len(words):
#            return words[n-1]
#    return("")

#print(get_word("This is a lesson about lists",4)) 

##########################################################

#def skip_elements(elements):
#    new_list = []
#    if len(elements) == 0:
#        return new_list
#    i = len(elements)
#    for x in range(i):
#        if x%2 == 0:
#            y = elements[x]
#            new_list.append(y)
#        x = x + 1
#        if x > i:
#            break
#    return new_list

#print(skip_elements(["a","b","c","d","e","f","g"]))

##########################################################

def skip_elements_again(elements):
    new1_list = []
    x = 0
    for index in enumerate(elements):
        if x % 2 == 0:
            new1_list.append(elements(x))
        x = x + 1
        if x > len(elements):
            break
    return new1_list

print(skip_elements_again(['a','b','c','d']))

