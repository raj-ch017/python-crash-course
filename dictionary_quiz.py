#def wardrobe_choice(wardrobe):
#    for items in wardrobe.keys():
#        for choices in wardrobe[items]:
#            print("The item {} is available in {} color".format(items,choices))

#wardrobe_choice({"shirt":['black','red','white'], "jeans":["blue","black"]})

##############################################################

#def email_list(domains):
#    emails = []
#    for domain in domains.keys():
#        for user in domains[domain]:
#            x = user + "@" + domain
#            emails.append(x)
#    return emails

#print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

#################################################################

def groups_per_user(group_dictionary):
    user_groups = {}
    grouping = []
    for group in group_dictionary.keys():
        for user in group_dictionary[group]:
            if user in user_groups:
                grouping.append(group)
                user_groups[user] = grouping
            else:
                user_groups[user] = group
    return user_groups

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))    
    
