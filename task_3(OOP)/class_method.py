#class methods = Allow operations related to the class itself
                # Take(cls) as the first parameter, which represents the claas itself
class Student:

    count = 0
    total_gpa = 0
    def __init__(self, name , gpa):
        self.name = name 
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa
    #INSTANCE METHOD    
    def get_info(self):
        return f"{self.name} : {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total no of student : {cls.count}"
    @classmethod
    def average_gpa(cls):
        return f"Average gpa of the class : {cls.total_gpa/cls.count:.2f}" if cls.count > 0 else "0" 
    



    
print(Student.get_count())
print(Student.average_gpa())

        