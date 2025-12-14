retry = 0
password = input("Enter your password: ")
while password != "secret":
    print("Incorrect password, try again.")
    password = input("Enter your password: ")
    retry += 1
    if retry >= 3:
        print("Too many incorrect attempts. Access denied.")
        break
        
else:
    print("Access Granted") 

    