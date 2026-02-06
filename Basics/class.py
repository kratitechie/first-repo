class user:
    def __init__ (self, name, age):
        self.name=name
        self.age=age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

        
        print (f"hello, my name is {self.name} and I am {self.age} years old")

u1=user(input("Enter name: "), int(input("Enter age: ")))
u1.display()