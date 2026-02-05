def math_ops(a,b):
    
    add= a + b
    sub= a - b
    if a>b:
        max_val= a
    else:
        max_val= b
    return add, sub, max_val
    
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

add, sub, max_val = math_ops(a,b)
print(add)
print(sub)
print(max_val)