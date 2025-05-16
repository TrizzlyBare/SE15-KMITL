import persistent
import BTrees


# Define the Student class
class Student(persistent.Persistent):
    def __init__(self, enrolls: list, id: int, name: str, password: str):
        self.enrolls = enrolls
        self.id = id
        self.name = name
        self.password = password

    def login(self, id, password):
        return (id == self.id) and (password == self.password)

    def enrollCourse(self, course):
        obj = Enrollment(course)
        self.enrolls.append(obj)
        return obj

    def getEnrollment(self, course):
        for item in self.enrolls:
            if item.course == course:
                return item
        return None

    def setName(self, name):
        self.name = name

    def printTranscript(self):
        print(f"    Transcript")
        print(f"ID: {self.id:>10} Name: {self.name:<20}")

        print(f"Course list")
        credit = 0
        credit_attempted = 0
        for enroll in self.enrolls:
            print(end="     ")
            enroll.printDetail()
            credit += convertGrade(enroll.getGrade()) * enroll.course.getCredit()
            credit_attempted += enroll.course.getCredit()

        print(
            f"Total GPA is: {credit/credit_attempted if credit_attempted != 0 else 0:.2f}"
        )


# Define the Course class
class Course(persistent.Persistent):
    def __init__(self, id, name, credit, gradeScheme):
        self.id = id
        self.name = name
        self.credit = credit
        self.gradeScheme = gradeScheme

    def getCredit(self):
        return self.credit

    def setName(self, name):
        self.name = name

    def scoreGrading(self, score):
        for entry in self.gradeScheme:
            if entry["min"] <= score <= entry["max"]:
                return entry["Grade"]
        raise Exception("Invalid score")

    def setGradeScheme(self, scheme):
        if not isinstance(scheme, list):
            raise Exception("Invalid Scheme")

        expected_grades = {"A", "B", "C", "D", "F"}
        found_grades = set()
        for entry in scheme:
            if not isinstance(entry, dict):
                raise Exception("Invalid Scheme")
            if ("Grade" not in entry) or ("min" not in entry) or ("max" not in entry):
                raise Exception("Invalid Scheme")
            found_grades.add(entry["Grade"])

        if found_grades == expected_grades:
            self.gradeScheme = scheme

    def printDetail(self):
        print(
            f"ID: {self.id:>8}   Course: {self.name:<32}, Credit {self.getCredit():>2}",
            end=" ",
        )


# Define the Enrollment class
class Enrollment(persistent.Persistent):
    def __init__(self, course, student="", score=0):
        self.course = course
        self.student = student
        self.score = score

    def getCourse(self):
        return self.course

    def getScore(self):
        return self.score

    def setScore(self, score):
        self.score = score

    def getGrade(self):
        return self.course.scoreGrading(self.score)

    def printDetail(self):
        self.course.printDetail()
        print(f"Score: {self.score:>3} Grade: {self.getGrade():>3}")


def convertGrade(grade):
    if grade == "A":
        return 4
    elif grade == "B+":
        return 3.5
    elif grade == "B":
        return 3
    elif grade == "C+":
        return 2.5
    elif grade == "C":
        return 2
    elif grade == "D+":
        return 1.5
    elif grade == "D":
        return 1
    else:
        return 0
