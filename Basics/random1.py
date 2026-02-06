import random

num = random.randint(1, 5)
guess = int(input("Guess a number between 1 and 5: "))

if guess == num:
    print("Correct!")
else:
    print("Wrong! Number was:", num)
