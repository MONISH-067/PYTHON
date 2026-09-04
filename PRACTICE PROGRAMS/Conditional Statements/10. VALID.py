email = input("Enter your email address: ")
if "@" in email and "." in email:
    print(f"{email} is a valid email address.")
else:
    print(f"{email} is not a valid email address.")