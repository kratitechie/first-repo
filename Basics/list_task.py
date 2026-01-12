number=[10,20,30,40,50]
total=0
for item in number:
    total=total+item

print("The list has these items:")
for item in number:
    print (item)
print("Total sum is:",total)
print("Average is:", total/len(number))