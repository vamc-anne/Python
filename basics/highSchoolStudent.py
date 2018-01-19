from Student import Student

class HighSchoolStudent(Student):
    def __init__(self, name, gender, grade):
        super(HighSchoolStudent, self).add_student(name, gender, grade)