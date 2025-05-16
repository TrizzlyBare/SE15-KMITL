import transaction
from ZODB import FileStorage, DB
from persistent import Persistent
from persistent.list import PersistentList
import BTrees._OOBTree
from BTrees._OOBTree import OOBTree


class Course(Persistent):
    def __init__(self, credit, id, name, gradeScheme={}):
        super().__init__()
        self.credit = credit
        self.id = id
        self.name = name
        self.gradeScheme = gradeScheme

    def getCredit(self):
        return self.credit

    def setName(self, name):
        self.name = name

    def scoreGrading(self, score):
        return f"ID: {self.id} Name: {self.name} Credit: {self.credit}"

    def setGradeScheme(self, scheme):
        self.gradeScheme = scheme

    def printDetail(self):
        print(f"ID:\t{self.id} Course: {self.name}\t, Credit: {self.credit}")


class Enrollment(Persistent):
    def __init__(self, course, student, score=0):
        super().__init__()
        self.course = course
        self.student = student
        self.score = score

    def getCourse(self):
        return self.course

    def getGrade(self):
        for grade in self.course.gradeScheme:
            if grade["min"] <= self.score <= grade["max"]:
                return grade["Grade"]
        return None

    def getScore(self):
        return self.score

    def setScore(self, score):
        self.score = score

    def printDetail(self):
        print(
            f"\tID:\t{self.course.id} Course: {self.course.name}\t, Credit: {self.course.credit} Score:  {int(self.score)} Grade: {self.getGrade()}"
        )


class Student(Persistent):
    def __init__(self, id, name="", password=""):
        super().__init__()
        self.enrolls = PersistentList()
        self.id = id
        self.name = name
        self.password = password

    def enrollCourse(self, course, score=0):
        enrollment = Enrollment(course, self, score)
        self.enrolls.append(enrollment)
        return enrollment

    def getEnrollment(self, course):
        for enrollment in self.enrolls:
            if enrollment.getCourse() == course:
                return enrollment
        return None

    def login(self, id, password):
        if self.id == id and self.password == password:
            return True
        else:
            return False

    def printTranscript(self):
        total_credits = 0
        total_grade_points = 0.0
        print(f"\tTranscript\nID:\t{self.id}  Name: {self.name}\nCourse list")
        for enrollment in self.enrolls:
            course = enrollment.getCourse()
            grade = enrollment.getGrade()
            enrollment.printDetail()
            if grade is not None:
                total_credits += course.getCredit()
                if grade == "A":
                    grade_points = 4.0
                elif grade == "B":
                    grade_points = 3.0
                elif grade == "C":
                    grade_points = 2.0
                elif grade == "D":
                    grade_points = 1.0
                elif grade == "F":
                    grade_points = 0.0
                else:
                    grade_points = 0.0

                total_grade_points += grade_points * course.getCredit()

        if total_credits > 0:
            gpa = total_grade_points / total_credits
            print(f"Total GPA is: {gpa:.2f}\n")
        else:
            print("No grades available to calculate GPA.\n")

    def getGpa(self):
        total_credits = 0
        total_grade_points = 0.0
        print(f"\tTranscript\nID:\t{self.id}  Name: {self.name}\nCourse list")
        for enrollment in self.enrolls:
            course = enrollment.getCourse()
            grade = enrollment.getGrade()
            enrollment.printDetail()
            if grade is not None:
                total_credits += course.getCredit()
                if grade == "A":
                    grade_points = 4.0
                elif grade == "B":
                    grade_points = 3.0
                elif grade == "C":
                    grade_points = 2.0
                elif grade == "D":
                    grade_points = 1.0
                elif grade == "F":
                    grade_points = 0.0
                else:
                    grade_points = 0.0

                total_grade_points += grade_points * course.getCredit()

        if total_credits > 0:
            gpa = total_grade_points / total_credits
            return gpa
        else:
            print("No grades available to calculate GPA.\n")

    def setName(self, name):
        self.name = name


storage = FileStorage.FileStorage("students_data.fs")
db = DB(storage)
connection = db.open()
root = connection.root()

if "courses" not in root:
    root["courses"] = OOBTree()

if "students" not in root:
    root["students"] = OOBTree()

grading = [
    {"Grade": "A", "min": 80, "max": 100},
    {"Grade": "B", "min": 70, "max": 79},
    {"Grade": "C", "min": 60, "max": 69},
    {"Grade": "D", "min": 50, "max": 59},
    {"Grade": "F", "min": 0, "max": 49},
]


def test_case():

    course1 = Course(4, "101", "Computer Programming", grading)
    course2 = Course(4, "201", "Web Programming", grading)
    course3 = Course(5, "202", "Software Engineering Principle", grading)
    course4 = Course(3, "301", "Artificial Intelligence", grading)

    root.courses = BTrees.OOBTree.BTree()
    root.courses[101] = course1
    root.courses[201] = course2
    root.courses[202] = course3
    root.courses[301] = course4

    student1 = Student(id=1101, name="Mr. Christian de Neuvillette", password="123")
    student2 = Student(id=1102, name="Mr. Zhong Li", password="123")
    student3 = Student(id=1103, name="Mr. Dvalinn Durinson", password="123")

    root["students"][1101] = student1
    root["students"][1102] = student2
    root["students"][1103] = student3

    student1.enrollCourse(course1, 85.0)
    student1.enrollCourse(course2, 73.0)
    student1.enrollCourse(course4, 60.0)

    student2.enrollCourse(course1, 90.0)
    student2.enrollCourse(course2, 78.0)
    student2.enrollCourse(course3, 67.0)

    student3.enrollCourse(course1, 55.0)
    student3.enrollCourse(course2, 80.0)
    student3.enrollCourse(course3, 45.0)
    student3.enrollCourse(course4, 89.0)

    transaction.commit()

    retrieved_course1 = root.courses[101]
    retrieved_course2 = root.courses[201]
    retrieved_course3 = root.courses[202]
    retrieved_course4 = root.courses[301]

    retrieved_course1.printDetail()
    retrieved_course2.printDetail()
    retrieved_course3.printDetail()
    retrieved_course4.printDetail()
    print("")

    for student_id in root["students"]:
        retrieved_student = root["students"][student_id]
        retrieved_student.printTranscript()


test_case()

transaction.commit()
connection.close()
db.close()
