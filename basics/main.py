from Student import Student
from fileOp import fileOp
from highSchoolStudent import HighSchoolStudent

def create_student():
    name = raw_input("Enter Students Name: ")
    gender = raw_input("Enter Students gender: ")        
    grade = raw_input("Enter Students grade: ")
    hss = HighSchoolStudent(name, gender, grade)
    print("{0} created as HighSchoolStudent".format(hss))
    

def get_students():
    students = fileOp.getData("student.txt")
    for student in students:
        print(student)

create_student()
get_students()

