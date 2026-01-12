while True:
    hey= int(input("Hey welcome to Kat&Nat, Please select the menu:\n 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Exit\n"))
    if hey==1:
        a= int(input("Enter first number:\n"))
        b= int(input("Enter second number:\n"))
        c=a+b
        print (f"The ans is  {c}.")

    elif hey==2:
        a= int(input("Enter first number:\n"))
        b= int(input("Enter second number:\n"))
        c=a-b
        print (f"The ans is  {c}.")     
    
    elif hey==3:
        a= int(input("Enter first number:\n"))
        b= int(input("Enter second number:\n"))
        c=a*b
        print (f"The ans is  {c}.")
    else:
        print("Exiting the menu. Goodbye!")
        break
