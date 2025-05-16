import ZODB, ZODB.FileStorage
import transaction
from persistent.mapping import (
    PersistentMapping,
)
from HW11_66011249_Tanakrit_models import Course, Student

storage = ZODB.FileStorage.FileStorage("mydata.fs")
db = ZODB.DB(storage)
connection = db.open()
root = connection.root()

if not hasattr(root, "courses"):
    root.courses = PersistentMapping()
if not hasattr(root, "students"):
    root.students = PersistentMapping()


def close_connection():
    connection.close()
    db.close()
