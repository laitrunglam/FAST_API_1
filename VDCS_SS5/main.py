from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

students = [
    {"id": 1, "name": "Nguyen Van A"},
    {"id": 2, "name": "Tran Thi B"},
    {"id": 3, "name": "Le Van C"}
]
courses = [
    {"id": 1, "name": "FastAPI Basic", "capacity": 2},
    {"id": 2, "name": "Python OOP", "capacity": 2}
]
registrations = [
    {"id": 1, "student_id": 1, "course_id": 1},
    {"id": 2, "student_id": 2, "course_id": 1}
]

app=FastAPI()

class Register(BaseModel):
    student_id: int
    course_id: int



@app.post('/registrations')
def get_check(register: Register):
    is_flag=0
    for i in students:
        if i['id']==register.student_id:
            is_flag=1
    if is_flag==0:
        raise HTTPException(
            status_code=404,
            detail='k ton tai tk id'
        )
    
    count_toida=0
    is_flag_0=0
    for i in courses:
        if i["id"]==register.course_id:
            count_toida=i['capacity']
            is_flag_0=1
    if is_flag_0==0:
        raise HTTPException(
            status_code=404,
            detail='k ton tai tk course'
        )
    
    for i in registrations:
        if i['student_id'] == register.student_id and i['course_id'] == register.course_id:
            raise HTTPException(
                status_code=409,
                detail="Student already registered this course"
            )
    

    cnt_dem=0
    for i in registrations:
        if i['course_id']==register.course_id:
            cnt_dem+=1

    if cnt_dem>=count_toida:
        raise HTTPException(
            status_code=400,
            detail="Course is full"
        )
    
    return register
