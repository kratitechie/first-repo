age = int(input("What is your age:\n"))

if age<13:
    print("you are a child")
elif age<=18:
    print("you are a teenager")
elif age>18 and age<60:
    print("you are an adult")
else:
    print("You are a senior citizen")
# This program checks if a user is eligible to vote based on their age.