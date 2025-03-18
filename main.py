from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, employee_id, department):
        self.__name = name  
        self.__employee_id = employee_id
        self.__department = department

    def display_details(self):
        """Display common employee details."""
        return f"ID: {self.__employee_id}, Name: {self.__name}, Department: {self.__department}"

    @abstractmethod
    def calculate_salary(self):
        """Abstract method to be implemented in subclasses."""
        pass

class PermanentEmployee(Employee):
    def __init__(self, name, employee_id, department, base_salary, bonus):
        super().__init__(name, employee_id, department)
        self.__base_salary = base_salary
        self.__bonus = bonus

    def calculate_salary(self):
        return self.__base_salary + self.__bonus


class ContractEmployee(Employee):
    def __init__(self, name, employee_id, department, hourly_rate, hours_worked):
        super().__init__(name, employee_id, department)
        self.__hourly_rate = hourly_rate
        self.__hours_worked = hours_worked

    def calculate_salary(self):
        return self.__hourly_rate * self.__hours_worked


class Intern(Employee):
    def __init__(self, name, employee_id, department, stipend):
        super().__init__(name, employee_id, department)
        self.__stipend = stipend

    def calculate_salary(self):
        return self.__stipend


def show_employee_salary(employee):
    print(f"{employee.display_details()}, Salary: ${employee.calculate_salary()}")


perm_emp = PermanentEmployee("Alice", 101, "IT", 5000, 1000)
contract_emp = ContractEmployee("Bob", 102, "HR", 50, 160)
intern_emp = Intern("Charlie", 103, "Finance", 1000)

show_employee_salary(perm_emp)
show_employee_salary(contract_emp)
show_employee_salary(intern_emp)

