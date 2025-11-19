def password(email, password):
    if "" not in password:
        print("need to be string")
        return
    if "@" not in email:
        print("missing a @!")
        return  
    if len(password)<8:
        print("password too short!(8)")
        return
    if not any(char.isdigit() for char in password):
        print("password needs at least 1 number")
        return
    if not any (char.isupper ()for char in password):
        print("must contain upper case")
        return
    print("ok email and pass good account is good")

print(password("test@gmail.com", "teFstx2fhgf"))
j