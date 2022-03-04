#def format_address(address_string):
#    list1 = address_string.split(" ")
#    house_number = list1[0]
#    list1.pop(0)
#    street_number = " ".join(list1)
#    print("house number {} is located on street {}".format(house_number,street_number))

#format_address("1001 1st Avenue")
#format_address("123 Main Street")
#format_address("55 North Centre Drive")

########################################################

#def combine_lists(list1,list2):
# list 1 belongs to Jamie, hence needs to be reversed
# list 2 belongs to Drew
# list 2 first, then list 1 reversed
#    first_list = list2
#    second_list = []
#    x = len(list1)
#    j = -1
#    for i in range(x):
#        a = list1[j]
#        second_list.append(a)
#        j = j - 1
#        if abs(j) > x:
#            break
#    final_list = first_list + second_list
#    print(final_list)

#combine_lists(["April", "March", "Feb", "Jan"],["hell"])

#############################################################

#def car_listing(car_prices):
#    result = ""
#    car_names = list(car_prices.keys())
#    for names in car_names:
#        b = car_prices[names]
#        print("{} costs ${}".format(names,b))

#car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000})

##############################################################

#def combine_guests(guests1,guests2):
# guests1 represents Rory's list
# guests2 represents Taylor's list
#    final_dict = {}
#    r_guestlist = list(guests1.keys())
#    t_guestlist = list(guests2.keys())
#    actual_guestlist = r_guestlist + t_guestlist
#    for names in actual_guestlist:
#        if names in guests1:
#            peeps_they_bring = guests1[names]
#            final_dict[names] = peeps_they_bring
#        elif names in guests2:
#            peeps_they_bring = guests2[names]
#            final_dict[names] = peeps_they_bring
#        if names in t_guestlist and names in r_guestlist:
#            b = guests1[names]
#            final_dict[names] = b
#    return final_dict

#Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
#Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

#print(combine_guests(Rorys_guests, Taylors_guests))

################################################################

def count_letters(text):
    result = {}
    text_lower = text.lower()
    text_in_list = text_lower.split()
    for words in text_in_list:
        for letter in words:
            if letter.isalpha():
                count = 1
                if letter not in result:
                    result[letter] = count
                else:
                    c = result[letter]
                    count = c + 1
                    result[letter] = count
    return result

print(count_letters("aAAbccDddddxyz!!!"))

