while True:
    number= int(input("Enter a number.\n"))
    if number<0:
        print(f'You entered a negative value: i.e. {number}. Please enter a posiitve number only.')
        continue
    print(f'You entered {number}. Thank you!')
    if number==0:
        print("You entered zero. Exiting the loop.")
        break   