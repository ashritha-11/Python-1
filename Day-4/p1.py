#create a class student
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def display(self):
        print("Name:", self.name, "Rollno:", self.roll_no, "Marks:", self.marks)
a = Student("Ashritha", "6708", "89")
b = Student("Akhila", "28", "95")
a.display()
b.display()
