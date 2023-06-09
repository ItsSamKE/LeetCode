
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def getGrade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def addStudent(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def getAverageGrade(self):
        value = 0
        for student in self.students:
            value += student.getGrade()
        return value / len(self.students)


s1 = Student('Sam', 32, 95)
s2 = Student('Alicia', 34, 87)
s3 = Student('Peter', 26, 75)

course = Course('Science', 2)
course.addStudent(s1)
course.addStudent(s2)
# print(course.students[0].name)
print(course.getAverageGrade())
