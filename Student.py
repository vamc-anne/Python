from fileOp import fileOp

class Student(object):
    students = []
    name = ""
    id = 0
    gender = ""
    grade = ""

    def add_student(self, name, gender = "F", grade = "1"):
        self.name = name
        self.gender = gender
        self.grade = grade
        fileOp.savedata("student.txt", name)

    def __str__(self):
        return self.name
  