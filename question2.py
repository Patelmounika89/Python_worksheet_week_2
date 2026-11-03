class Employee:
    def __init__(self,employee_id,employee_name,salary):
        self.employee_id=employee_id
        self.employee_name=employee_name
        self.salary=salary
    def display_details(self):
        print("Employee Name:",self.employee_id)
        print("Employee ID:",self.employee_name)
        print("Salary:",self.salary)
emp1=Employee("Mounika",1001,35000)
emp2=Employee("Kavya",1002,40000)
emp3=Employee("Sneha",1003,25000)
emp1.display_details()
emp2.display_details()
emp3.display_details()