# Employ Bonus Calculator

class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def calculate_bonus(self, performance_rating):
        if performance_rating == "excellent":
            return self.salary * 0.20
        elif performance_rating == "good":
            return self.salary * 0.10
        else:
            return 0

employee = Employee("Alice", 101, 50000)
bonus = employee.calculate_bonus("excellent")
print(f"Yearly bonus for {employee.name} is: {bonus}")