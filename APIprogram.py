from fastapi import FastAPI

app = FastAPI()
students = [
    {
        "id": 1,
        "name": "Ram",
        "course": "Python",
        "marks": 85
    },
    {
        "id": 2,
        "name": "Diya",
        "course": "AI",
        "marks": 90
    }
]


@app.post("/students")
def create_student(name: str, course: str, marks: int):

    student = {
        "name": name,
        "course": course,
        "marks": marks
    }

    return {
        "message": "Student created successfully",

        "student": student
    }
# GET ENDPOINT
@app.get("/students")
def get_students():

    return students