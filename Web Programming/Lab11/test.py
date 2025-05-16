import ZODB, ZODB.FileStorage
import transaction
import BTrees
from database import Student, Course, Enrollment, convertGrade

# Main Code
if __name__ == "__main__":
    # Setup ZODB database
    storage = ZODB.FileStorage.FileStorage("mydata.fs")
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root
    root.students = BTrees.OOBTree.BTree()
    root.courses = BTrees.OOBTree.BTree()

    # Define grading schemes
    scheme1 = [
        {"Grade": "A", "min": 80, "max": 100},
        {"Grade": "B", "min": 70, "max": 79},
        {"Grade": "C", "min": 60, "max": 69},
        {"Grade": "D", "min": 50, "max": 59},
        {"Grade": "F", "min": 0, "max": 49},
    ]

    scheme2 = [
        {"Grade": "A", "min": 85, "max": 100},
        {"Grade": "B", "min": 70, "max": 84},
        {"Grade": "C", "min": 60, "max": 69},
        {"Grade": "D", "min": 50, "max": 59},
        {"Grade": "F", "min": 0, "max": 49},
    ]

    scheme3 = [
        {"Grade": "A", "min": 80, "max": 100},
        {"Grade": "B", "min": 70, "max": 79},
        {"Grade": "C", "min": 55, "max": 69},
        {"Grade": "D", "min": 50, "max": 54},
        {"Grade": "F", "min": 0, "max": 49},
    ]

    # Add courses to the database
    root.courses[101] = Course(101, "Computer Programming", 4, scheme1)
    root.courses[201] = Course(201, "Web Programming", 4, scheme1)
    root.courses[202] = Course(202, "Software Engineering Principle", 5, scheme2)
    root.courses[301] = Course(301, "Artificial Intelligence", 3, scheme3)

    # Add students to the database
    root.students[112] = Student([], 112, "Mr. Christian de Neuvillette", "test")
    root.students[112].enrollCourse(root.courses[101])
    root.students[112].enrollCourse(root.courses[201])
    root.students[112].enrollCourse(root.courses[202])
    root.students[112].enrollCourse(root.courses[301])

    root.students[112].enrolls[0].setScore(71)
    root.students[112].enrolls[1].setScore(71)
    root.students[112].enrolls[2].setScore(69)
    root.students[112].enrolls[3].setScore(90)

    root.students[123] = Student([], 123, "Mr. Zhong Li", "test")
    root.students[123].enrollCourse(root.courses[101])
    root.students[123].enrollCourse(root.courses[201])
    root.students[123].enrollCourse(root.courses[202])
    root.students[123].enrollCourse(root.courses[301])

    root.students[123].enrolls[0].setScore(90)
    root.students[123].enrolls[1].setScore(50)
    root.students[123].enrolls[2].setScore(70)
    root.students[123].enrolls[3].setScore(60)

    root.students[234] = Student([], 234, "Mr. Dvalinn Durison", "test")
    root.students[234].enrollCourse(root.courses[101])
    root.students[234].enrollCourse(root.courses[201])
    root.students[234].enrollCourse(root.courses[202])
    root.students[234].enrollCourse(root.courses[301])

    root.students[234].enrolls[0].setScore(90)
    root.students[234].enrolls[1].setScore(50)
    root.students[234].enrolls[2].setScore(70)
    root.students[234].enrolls[3].setScore(60)

    # Commit the transaction
    transaction.commit()

    # Print course details
    courses = root.courses
    for c in courses:
        course = courses[c]
        course.printDetail()
        print()

    print()

    # Print student transcripts
    students = root.students
    for s in students:
        student = students[s]
        student.printTranscript()
        print()

    # Close the ZODB connection
    connection.close()
    db.close()
