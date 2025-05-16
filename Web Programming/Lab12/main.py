import ZODB
import ZODB.FileStorage
import persistent
import transaction
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from models import Course, Student  # Ensure this matches your module name

storage = ZODB.FileStorage.FileStorage("students_data.fs")
db = ZODB.DB(storage)
connection = db.open()
root = connection.root()

app = FastAPI()


# Service A - GET: Display Login Page
@app.get("/login", response_class=HTMLResponse)
async def login_page():
    html_content = """
    <html>
        <head><title>Login</title></head>
        <body>
            <h1>Login Page</h1>
            <form method="post" action="/login">
                <label for="id">ID:</label>
                <input type="text" name="id" id="id" required><br><br>
                <label for="password">Password:</label>
                <input type="password" name="password" id="password" required><br><br>
                <input type="submit" value="Login">
            </form>
        </body>
    """
    return HTMLResponse(content=html_content)


# Service B - POST: Handle Login and Redirect
@app.post("/login", response_class=HTMLResponse)
async def login(id: int = Form(...), password: str = Form(...)):
    student = root["students"].get(id)

    if student and student.login(id, password):
        return RedirectResponse(url=f"/update_scores/{id}", status_code=303)
    else:
        html_content = """
        <html>
            <body>
                <h1>Login Failed</h1>
                <p>Incorrect ID or password.</p>
                <a href="/login">Try Again</a>
            </body>
        </html>
        """
        return HTMLResponse(content=html_content)


# Service C - GET: Display Score Update Page
@app.get("/update_scores/{student_id}", response_class=HTMLResponse)
async def update_scores(student_id: int):
    student = root["students"].get(student_id)
    if not student:
        return HTMLResponse(content="<h1>Student not found</h1>")

    html_content = f"""
        <html>
            <head><title>Transcript Enter Form</title></head>
            <body>
                <h1>Transcript Entry Form</h1>
                <table border="1" cellpadding="10"> 
                <thead>
                <th>ID: {student.id}</th>
                <th>Name: {student.name}</th>
                <form method="post" action="/submit_scores/{student.id}">
                </thead>
                </table>
                <table border="1" cellpadding="10">
                    <thead>
                        <tr>
                            <th>Course Code</th>
                            <th>Course Name</th>
                            <th>Credits</th>
                            <th>Score</th>
                        </tr>
                    </thead>
                    <tbody>
    """

    # Dynamically generate rows for each course the student is enrolled in
    for enrollment in student.enrolls:
        html_content += f"""
            <tr>
                <td>{enrollment.course.id}</td>
                <td>{enrollment.course.name}</td>
                <td>{enrollment.course.credit}</td>
                <td><input type="number" name="course_{enrollment.course.id}" value="{enrollment.getScore()}" required></td>
            </tr>
        """

    html_content += """
                    </tbody>
                </table>
                <br>
                <input type="submit" value="Submit Scores">
            </form>
        </body>
    </html>
    """

    return HTMLResponse(content=html_content)


# Service C - POST: Submit Scores and Redirect to Transcript
@app.post("/submit_scores/{student_id}", response_class=HTMLResponse)
async def submit_scores(student_id: int, request: Request):
    student = root["students"].get(student_id)
    if not student:
        return HTMLResponse(content="<h1>Student not found</h1>")

    form_data = await request.form()

    for enrollment in student.enrolls:
        score_key = f"course_{enrollment.course.id}"
        if score_key in form_data:
            score = float(form_data[score_key])
            enrollment.setScore(score)

    transaction.commit()  # Save the updated scores to the database

    return RedirectResponse(url=f"/transcript/{student_id}", status_code=303)


@app.get("/transcript/{student_id}", response_class=HTMLResponse)
async def transcript(student_id: int):
    student = root["students"].get(student_id)
    if not student:
        return HTMLResponse(content="<h1>Student not found</h1>")

    html_content = f"""
    <html>
        <head>
            <title>Transcript</title>
            <style>
                table {{
                    border-collapse: collapse;
                    width: 100%;
                }}
                th, td {{
                    padding: 10px;
                    text-align: left;
                }}
                th {{
                    background-color: #f2f2f2;
                }}
                tr {{
                    border: none;  /* No horizontal borders */
                }}
            </style>
        </head>
        <body>
            <h1>(Unofficial Transcript)</h1>
            <h2>School of Engineering</h2>
            <p>Name:&nbsp{student.name}&nbsp&nbsp&nbsp&nbsp&nbspStudent ID:&nbsp{student.id}</p>
            <table>
                <thead>
                    <tr>
                        <th>Course Title</th>
                        <th>Credits</th>
                        <th>Score</th>
                        <th>Grade</th>
                    </tr>
                </thead>
                <tbody>
    """

    for enrollment in student.enrolls:
        html_content += f"""
            <tr>
                <td>{enrollment.course.name}</td>
                <td>{enrollment.course.credit}</td>
                <td>{enrollment.getScore()}</td>
                <td>{enrollment.getGrade()}</td>
            </tr>
        """

    html_content += f"""
                </tbody>
            </table>
            <h3>GPA: {student.getGpa():.2f}</h3>
        </body>
    </html>
    """

    return HTMLResponse(content=html_content)


# Main
if __name__ == "__main__":
    transaction.commit()
    connection.close()
    db.close()
