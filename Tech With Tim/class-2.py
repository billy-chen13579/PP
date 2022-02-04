class Student:
    def __init__(self, name ,age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        
    def add_students(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average(self):
        value=0
        for student in self.students:
            value += student.get_grade() #student is in the class Student, so we can run the function get_grade()
        return value / len(self.students)

s1 = Student("Tim", 19, 95)
s2 = Student("Billy", 19, 100)
s3 = Student("Jill",19, 60)

course = Course("Science", 2)
course.add_students(s1)
course.add_students(s2)
print(course.add_students(s3)) # return False, because the maximum students of this course is only 2

print(course.get_average()) # not include s3