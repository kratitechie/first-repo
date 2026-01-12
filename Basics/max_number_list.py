number = []

for i in range(5):
    x = int(input("Enter a number: "))
    number.append(x)


max_num=number[0]

for item in number:
    if item>max_num:
        max_num=item

print("The maximum number in the list is:", max_num)