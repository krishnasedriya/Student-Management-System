# Student-Management-System
students = []

while True:
    print("press:\n For Adding a new student\n FOr Show all\n For Report card\n For Update\n For Exit:")
    choice = int(input())
    if choice == 1:
        name = input("Enter Student Name:")
        print("\n===================")
        age = int(input("Enter Student Age:"))
        print("\n===================")
        marks = int(input("Enter Student Marks:"))
        S = {
            "name":name,
            "age":age,
            "marks":marks
        }
        students.append(S)
    elif choice == 2:
        for student in students:
            print("--------------------------")
            print("name:", student["name"])
            print("age:", student["age"])
            print("marks:", student["marks"])
            if student["marks"] > 85:
                print("Grade: A")
            elif student["marks"] > 70:
                print("Grade: B")
            elif student["marks"] > 55:
                print("Grade: C")
            elif student["marks"] > 40:
                print("Grade: D")
            else:
                print("Grade: Fail")
            print("--------------------------")
    elif choice == 3:
        maxMarks = students[0]["marks"]
        maxMarksName = students[0]["name"]
        minMarks = students[0]["marks"]
        minMarksName = students[0]["name"]
        totalPassCount = 0
        for student in students:
            if student["marks"] > maxMarks:
                maxMarks = student["marks"]
                maxMarksName = student["name"]
            if student["marks"] < minMarks:
                minMarks = student["marks"]
                minMarksName = student["name"]
            if student["marks"] >= 40:
                totalPassCount += 1
        print("\n===================")
        print(f"{maxMarksName} has scored highest in class which is  {maxMarks}:")
        print(f"{minMarksName} has scored lowest in class which is {minMarks}:")
        print("total pass count:", totalPassCount)
        print("percentage:",totalPassCount/len(students)*100,"%")
        print("\n===================")
    elif choice == 4:
        print("\n===================")
        nameOfStudent = input("Enter Student Name you want to update:")
        print("----------------------------------")
        name = input("Enter Student Name:")
        age = int(input("Enter Student Age:"))
        marks = int(input("Enter Student Marks:"))
        newData = {
            "name":name,
            "age":age,
            "marks":marks
        }
        for student in range(len(students)):
            if students[student]["name"] == nameOfStudent:
                students[student]["name"] = newData["name"]
                students[student]["marks"] = newData["marks"]
                students[student]["age"] = newData["age"]
                break
            print( "updating..")
        print("\n===================")
    elif choice == 5:
        print("\n===================")
        print("Exiting Program")
        print("\n===================")
        break
    else:
        print("\n===================")
        print("Invalid choice...")
        print("\n===================")


