def password(email, password):
    if "@" not in email:
        print("missing a @!")
        return  
    if len(password)<8:
        print("password too short!(8)")
        return
    if password == password.lower:
        print("must use cap letter")
    print("ok email and pass good")

print(password("test@gmail.com", "testoooooo"))