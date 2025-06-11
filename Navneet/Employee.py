class Employee:
    def __init__(self, id, name, designation, department):
        print("Calling Constructor : Before")
        print("id : ", id)
        print("name : ", name)
        print("designation : ", designation)
        print("department : ", department)
        self.id = id
        self.name = name
        self.designation = designation
        self.department = department
        print("-" * 20)
        print("Calling Constructor : After")
        print("id : ", id)
        print("name : ", name)
        print("designation : ", designation)
        print("department : ", department)

    def display(self):
        print("id : ", self.id)
        print("name : ", self.name)
        print("designation : ", self.designation)
        print("department : ", self.department)


emp1 = Employee(101, "navneet ranjan", "manager", "finance")
print("-" * 20)
print("id : ", emp1.id)
print("id : ", emp1.name)
print("id : ", emp1.designation)
print("id : ", emp1.department)
print("-" * 20)
print("Calling display() method")
emp1.display()