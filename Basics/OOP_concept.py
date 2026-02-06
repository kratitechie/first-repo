class animal():
    def speak(self):
        print("Animal makes a sound")

class dog(animal): #Inheritance (class uses properties and methods of parent class))
    def speak(self): #polymorphism (same method name but different implementation)
        print("Dog barks")

class cat(animal):
    def speak(self):
        print ("cat meows")

a=animal()
d=dog()
c=cat()

a.speak() #animal making a sound
d.speak() #dog barks 
c.speak() #cat meows