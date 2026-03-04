class Employee:
    def __init__(self, name ,salary):
        self.name = name
        self.salary = salary

    def get_annual_salary(self):
        return self.salary* 12
    
    def display_info(self):
        print(f"name: {self.name}")
        print(f"salary: {self.salary}")
        print(f"annual salary: {self.get_annual_salary()}")

# emp1 = Employee("Mariam", 10000)
# emp1.display_info()