found_list={
    'name': 'Krati',
    'age': 21
}

key_find=input("Enter key to be found:\n")


found=False
for key in found_list:
    if key==key_find:
        found=True
        print("Key is found")
        break
    found_list = {
    'name': 'Krati',
    'age': 21
}

key_find = input("Enter key to be found:\n")

found = False

for key in found_list:
    if key == key_find:
        found = True
        print("Key is found")
        break

if not found:
    print("Key is not found")
