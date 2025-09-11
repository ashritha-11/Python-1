#Employee and Manager
class Employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print("Employee name:",self.name,"Employee salary:",self.salary)
class Manager(Employee):
    def __init__(self,department):
        self.department=department
    def display(self):
        print("Employee department:",self.department)
a=Employee("Ashritha","50000")
b=Manager("CSD")
a.display()
b.display()
    
