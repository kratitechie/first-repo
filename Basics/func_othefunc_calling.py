def is_even(n):
    if n%2==0:
        return True
    else:
        return False
    
    # return True or False

def even_message(n):
    if is_even(n):
        return f'{n} is an even number.'
    else:
        return f'{n} is an odd number.'
    # call is_even here and return message

num = int(input("Enter a number: "))
msg = even_message(num)
print(msg)
