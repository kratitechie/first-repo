while True:
    password= input("Enter the password: ")
    
    if password=="Admin123":
        print(" Access granted. Redirecting to home page.")
        break
    else:
        print(" Incorrect password. Try again.")
