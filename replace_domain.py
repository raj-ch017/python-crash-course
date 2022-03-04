def replace_domain(email,old_domain,new_domain):
    if "@" + old_domain in email:
        index = email.index("@")
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email

print(replace_domain("raj.utd@google.com","google.com","gmail.com"))
print(replace_domain("soumya.das@gmail.com","google.com","gmail.com"))