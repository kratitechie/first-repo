def my_map(my_func,my_iterable):
    result=[]
    for item in my_iterable:
        new_item= my_func(item)
        result.append(new_item)
    return(result)

nums=[1,2,3,4,5]
square=my_map(lambda x:x**2, nums)

print(square)