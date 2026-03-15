class Student:

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

student = Student("Claudia", 123)
student.enroll("Applied Math")
student.enroll("Economics")
student.name = "Sophia"
print(student)
print(student.name)
print(student.courses)