import ZODB, ZODB.FileStorage
import transaction
from persistent.mapping import PersistentMapping
from models import Course, Student
from main import root, close_connection

if __name__ == "__main__":
    # Adding courses
    if "101" not in root.courses:
        root.courses["101"] = Course("101", "Computer Programming", 4)
    if "201" not in root.courses:
        root.courses["201"] = Course("201", "Web Programming", 4)
    if "202" not in root.courses:
        root.courses["202"] = Course("202", "Software Engineering Principle", 5)
    if "301" not in root.courses:
        root.courses["301"] = Course("301", "Artificial Intelligence", 3)

    # Adding students
    if "1101" not in root.students:
        root.students["1101"] = Student("1101", "Mr. Christian de Neuvillette", "1234")
    if "1102" not in root.students:
        root.students["1102"] = Student("1102", "Mr. Zhong Li", "12345")
    if "1103" not in root.students:
        root.students["1103"] = Student("1103", "Mr. Dvalinn Durinson", "123456")

    # Enroll students and set grades
    student1 = root.students["1101"]
    if not student1.enrolls:
        student1.enrollCourse(root.courses["101"]).setScore(85)
        student1.enrollCourse(root.courses["201"]).setScore(75)
        student1.enrollCourse(root.courses["301"]).setScore(65)

    student2 = root.students["1102"]
    if not student2.enrolls:
        student2.enrollCourse(root.courses["101"]).setScore(95)
        student2.enrollCourse(root.courses["201"]).setScore(85)
        student2.enrollCourse(root.courses["202"]).setScore(55)

    student3 = root.students["1103"]
    if not student3.enrolls:
        student3.enrollCourse(root.courses["101"]).setScore(65)
        student3.enrollCourse(root.courses["201"]).setScore(95)
        student3.enrollCourse(root.courses["202"]).setScore(75)
        student3.enrollCourse(root.courses["301"]).setScore(65)

    # Commit the transaction
    transaction.commit()

    # Printing course details
    print("================ RESTART: pythoncode ================")
    for course in root.courses.values():
        if isinstance(course, Course):
            course.printDetail()
        else:
            print("Not a Course object:", course)

    print()

    # Printing student transcripts
    for student in root.students.values():
        student.printTranscript()
        print()

    # Close connection after all operations
    close_connection()
