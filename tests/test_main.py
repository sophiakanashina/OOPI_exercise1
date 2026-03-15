from exercise1.exercises import Student

def test_enrollment():
    student = Student("Claudia", 123)
    len1 = len(student.courses)
    student.enroll("course1")
    len2 = len(student.courses)
    assert len2 - len1 == 1
