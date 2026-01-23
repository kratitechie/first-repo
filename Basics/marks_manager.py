#program to understand different list methods in python
marks=[]

while True:
    print("\nChoose an operation to perform on the marks list:")
    print("1. Add Marks")
    print("2. Insert a mark at position")
    print("3. Remove a mark")
    print("4. Pop last mark")
    print("5. Sort marks")
    print("6. Show top 3 marks")
    print("7. Show all marks")
    print("8. Exit")

    choice = input("Enter your choice(1-8): ")
    if choice == "1":
        m = int(input("Add marks to be added to list: "))
        marks.append(m)
        print("Marks added.")

    elif choice== "2":
        pos= int(input("Enter a position to enter tha marks: "))
        m=int(input("Enter the marks to be inserted: "))
        marks.insert(pos, m)
        print("Marks inserted.")
        print(marks)

    elif choice=="3":
        m=int(input("Enter the marks to be removed: "))
        if m in marks:
            marks.remove(m)
            print("Marks removed.")
        else:
            print("Marks not found in the list.")
        
    elif choice== "4":
        if marks:
            removed = marks.pop()
            print(f"Removed mark: {removed}")
        else:
            print("List is empty!")


    elif choice== "5":
        marks.sort()
        print("Marks sorted.")

    elif choice== "6":
        top_marks=marks[-3:]
        print("Top 3 marks are:", top_marks)

    elif choice== "7":
        print("Current marks list:", marks)
    elif choice== "8":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")


