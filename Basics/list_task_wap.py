number=[]
for i in range(5):
    no= int(input("enter a number for list:\n"))
    number.append(no)

print("The list is:", number)

#Maximum number
max_num=number[0]
for item in number:
    if item>max_num:
        max_num=item
print("The maximum number in the list is:", max_num)

#Smallest Number
small_num=  number[0]

for item in number:
    if small_num>item:
        small_num=item
print("The smallest number in the list is:", small_num)

search_want=input("Do you want to search for a number in the list? (yes/no):\n")
if search_want.lower()=="yes":
    search= int(input("enter a number to find:\n"))
    found= False
    for item in number:
        if item==search:
            found=True
            break
    if found== True:
        print("Your number is found in the list.")
    else:
        print("Your number is not found in the list.")

