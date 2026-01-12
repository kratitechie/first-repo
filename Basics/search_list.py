number = []

for i in range(5):
    x = int(input("Enter a number: "))
    number.append(x)

search= int(input("Enter a number to find: "))
found=False
for item in number:
    if item==search:
        found=True
        break

if found==True:
    print('Your number is found in the list.')
else:
    print('Your number is not found in the list.')  