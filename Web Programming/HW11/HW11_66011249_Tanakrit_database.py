import transaction
from ZODB import FileStorage, DB
from BTrees._OOBTree import OOBTree
from HW11_66011249_Tanakrit_models import Course, Student

# Set up the database
storage = FileStorage.FileStorage("students_data.fs")
db = DB(storage)
connection = db.open()
root = connection.root()

# Check if the 'courses' and 'students' keys exist in the root object
if "courses" not in root:
    root["courses"] = OOBTree()  # Use OOBTree instead of direct attribute access

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

    # Store courses in the 'courses' OOBTree
    root["courses"][101] = course1
    root["courses"][201] = course2
    root["courses"][202] = course3
    root["courses"][301] = course4

    # Create and store students in the 'students' OOBTree
    student1 = Student(id=1101, name="Mr. Christian de Neuvillette")
    student2 = Student(id=1102, name="Mr. Zhong Li")
    student3 = Student(id=1103, name="Mr. Dvalinn Durinson")

    root["students"][1101] = student1
    root["students"][1102] = student2
    root["students"][1103] = student3

    # Enroll students in courses
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

    # Print out student transcripts
    for student_id in root["students"]:
        retrieved_student = root["students"][student_id]
        retrieved_student.printTranscript()


test_case()

# Commit and close the transaction
transaction.commit()
connection.close()
db.close()
