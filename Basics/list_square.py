numbers=[1,2,3,4]
square=[]
for num in numbers:
    square.append(num**2)
print("The squares are:", square)





even=[num*num for num in numbers if num%2==0]
print("The squares using list comprehension are:", even)