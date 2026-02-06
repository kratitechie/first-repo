from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class rectangle(shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
r1=rectangle(int(input("Enter width: ")), int(input("Enter height: ")))
print("Area of rectangle: ", r1.area())

