import requests

url = "http://161.246.5.62:11249/students/html/"


def get_all_students():
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("Request successful")
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


def get_student_by_id(student_id):
    student_url = f"{url}{student_id}/"
    try:
        response = requests.get(student_url)
        response.raise_for_status()
        print(f"Request successful for student ID {student_id}")
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error for student ID {student_id}: {e}")


name = input("Enter name: ")
surname = input("Enter surname: ")
student_id = input("Enter student ID: ")

data = {"name": name, "surname": surname, "ID": student_id}

try:
    response = requests.post("http://161.246.5.62:11249/students/new/", json=data)
    response.raise_for_status()
    print("Request successful")
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

get_all_students()
get_student_by_id(student_id)
