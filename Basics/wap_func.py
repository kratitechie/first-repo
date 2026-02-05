print("Hello and welcome to the world of Python functions!")

def data(name, birth_year):   # removed age parameter
    age = 2026 - birth_year
    print(f"hello {name}, your age is {age}")

name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
data(name=name, birth_year=birth_year)   # removed age argument

