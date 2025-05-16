import persistent
from persistent.list import PersistentList


class Course(persistent.Persistent):
    def __init__(self, credit, id, name, gradeScheme={}):
        self.credit = credit
        self.id = id
        self.name = name
        self.gradeScheme = gradeScheme

    def __str__(self):
        return "ID: %d Course: %s, Credit: %d" % (self.id, self.name, self.credit)

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


class Enrollment(persistent.Persistent):
    def __init__(self, course, student, score=0):
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


class Student(persistent.Persistent):
    def __init__(self, id, name=""):
        self.enrolls = PersistentList()
        self.id = id
        self.name = name

    def enrollCourse(self, course, score=0):
        enrollment = Enrollment(course, self, score)
        self.enrolls.append(enrollment)
        return enrollment

    def getEnrollment(self, course):
        for enrollment in self.enrolls:
            if enrollment.getCourse() == course:
                return enrollment
        return None

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

    def setName(self, name):
        self.name = name
