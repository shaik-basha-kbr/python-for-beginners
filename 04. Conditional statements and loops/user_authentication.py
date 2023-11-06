username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "secret":
    print("Access granted.")
else:
    print("Access denied.")
