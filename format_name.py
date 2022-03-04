def format_name(first_name,last_name):
    if len(first_name) > 0 and len(last_name) > 0:
        name = "Name: " + last_name + ", " + first_name
        return name
    elif len(first_name)==0 and len(last_name) > 0:
        name = "Name: " + last_name
        return name
    elif len(first_name) > 0 and len(last_name)==0:
        name = "Name: " + first_name
        return name
    else:
        return ""

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string