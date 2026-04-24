#static method + a method that doesn't need the instance, and only belongs to the class
#usually used for general utility functions

#Instance methods = Best for operations on instances of the class(obj)
#Static methods = best for utility functions that do not need access to the class data

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    @staticmethod
    def verify_position(position):
        valid_position= ["Manage","Cook","Cashier","Janitor"]
        return position in valid_position
    

print(Employee.verify_position("Cook"))