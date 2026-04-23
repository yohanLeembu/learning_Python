# Nested class = a class defined within another class
#                 class Outer:
#                         class inner:
                                
# benifits: allows you to logically group classes that are closely related
#             Encapsulates private details that aren't relevant outside of the outer class
#             keeps the namespace clean; reduces the possibility of naming conflicts
class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position
        def display_details(self):
            return f"Name:{self.name} Position:{self.position}"

    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)

    def list_employee(self):
        return [employee.display_details() for employee in self.employees]


company = Company("Straw Hat")

company.add_employee("Nami","Navigator")
company.add_employee("Usoop","Sniper")
company.add_employee("Sanji","Cook")
company.add_employee("Zoro","Swordsman")



for employee in company.list_employee():
    print(employee)

