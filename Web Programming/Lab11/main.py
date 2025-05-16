import ZODB, ZODB.FileStorage
import transaction
from database import *

# Open the database connection
storage = ZODB.FileStorage.FileStorage("mydata.fs")
db = ZODB.DB(storage)
connection = db.open()
root = connection.root()

if __name__ == "__main__":
    # Print all students' transcripts
    students = root.students
    for s in students:
        student = students[s]
        student.print_transcript()
        print()

    # Close the connection after running
    connection.close()
    db.close()
