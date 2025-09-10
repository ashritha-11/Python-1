def school():
    n = int(input("Enter number of students: "))
    students = []

    for i in range(n):
        rollno = int(input("Enter rollno: "))
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        students.append((rollno, name, marks))

    print("\nList of tuples:", students)
    highest = students[0][2]   
    for s in students:
        if s[2] > highest:
            highest = s[2]

    print("Highest scored marks:", highest)
    print("\nStudents scoring above 75:")
    for s in students:
        if s[2] > 75:
            print("RollNo:", s[0], "Name:", s[1], "Marks:", s[2])


school()
