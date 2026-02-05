try:
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    operation=input("Enter operation (+, -, *,  /): ") 

    if operation=='+':
        result=a+b
    elif operation=='-':
        result=a-b
    elif operation=='*':
        result=a*b
    elif operation=='/':
        result=a/b
    else:
        print("Invalid operation!")
        result=None

except ValueError:
    print("Invalid input! Please enter numeric values.")
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")

else:
    if result is not None:

        print(f"The result of {a} {operation} {b} is: {result}")
finally:
    print("Execution completed.") 
