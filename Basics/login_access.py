print("Hey how are we doing today\n")
age= int(input("What is your age? \n"))
country= input("Which country are you from? \n").lower()
if age >=18 and country == "india" or country== "usa":
    print("You are allowed to log in")
else:
    print("You are not allowed to log in")
