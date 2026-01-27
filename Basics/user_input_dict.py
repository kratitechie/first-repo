student={}
name=input("enter your name:")
age=int(input("enter your age:"))

student['name']= name 
student['age']=age 

print("Student details are:/n ")

for key, value in student.items():
    print(key, ":", value)