class Person:
    def __init__(self, name, age):
        self.name = name  # Attribute from Person class
        self.age = age    # Attribute from Person class

    def display_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Employee:
    def __init__(self, employee_id, department):
        self.employee_id = employee_id  # Attribute from Employee class
        self.department = department    # Attribute from Employee class

    def display_employee_info(self):
        print(f"Employee ID: {self.employee_id}, Department: {self.department}")


class Manager(Person, Employee):
    def __init__(self, name, age, employee_id, department, team_size):
        # Call constructors of both parent classes
        Person.__init__(self, name, age)
        Employee.__init__(self, employee_id, department)
        self.team_size = team_size  # Additional attribute for Manager class

    def display_manager_info(self):
        # Display info from all parent classes and manager-specific info
        self.display_person_info()
        self.display_employee_info()
        print(f"Team Size: {self.team_size}")


# Example Usage
manager = Manager("Alice", 35, "E123", "IT", 10)

# Access all attributes and methods
manager.display_manager_info()
