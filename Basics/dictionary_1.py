student={
    "name":"Krati",
    "age":26,
    "gender":"female"
}
student["city"]= "Indore"

print("student details:\n")
for key, value in student.items():
    print(key, ":", value)