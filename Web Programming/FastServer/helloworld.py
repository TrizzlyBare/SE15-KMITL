from fastapi import FASTAPI

app = FASTAPI()


students = {
    "29": {"ID": 29, "first_name": "Kazuha", "last_name": "Kaedehara"},
    "30": {"ID": 30, "first_name": "Albedo", "last_name": "Rhinedottir"},
}


@app.get("/students/all")
async def get_students():
    return students


@app.get("/students/{student_id}")
async def get_student(student_id: str):
    if student_id in students:
        return students[student_id]
    return {"error": "Student not found"}


@app.post("/students/new")
async def create_student(student: dict):
    student_id = student["ID"]
    if student_id in students:
        return {"error": "Student already exists"}
    students[student_id] = student
    return student


@app.post("/students/new/{student_id}")
async def create_student(student_id: str, student: dict):
    if student_id in students:
        return {"error": "Student already exists"}
    students[student_id] = student
    return student


@app.post("/students/new/")
async def create_student(
    student_first_name: str, student_last_name: str, student_id: str
):
    if student_id in students:
        return {"error": "Student already exists"}
    students[student_id] = {
        "ID": student_id,
        "first_name": student_first_name,
        "last_name": student_last_name,
    }
    return students[student_id]
