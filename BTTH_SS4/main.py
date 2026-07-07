from fastapi import FastAPI,Query
from typing import Optional

app=FastAPI()


courses = [
    {
        "id": 1,
        "name": "Python Basic",
        "category": "backend",
        "price": 3000000,
        "mode": "online"
    },
    {
        "id": 2,
        "name": "Java Web",
        "category": "backend",
        "price": 5000000,
        "mode": "offline"
    },
    {
        "id": 3,
        "name": "Web Frontend",
        "category": "frontend",
        "price": 4000000,
        "mode": "online"
    }
]

@app.get('/courses')
def get_courses():
    return courses

@app.get('/courses/search')
def search_courses(
    mode: Optional[str] = Query(None,description='Lọc theo hình thức học: online/offline'),
    category: Optional[str] = Query(None,description='Lọc theo nhóm khóa học: backend/frontend')
):
    lst=courses
    # if mode: 
    #     lst1=[]
    #     for i in lst:
    #         if mode==i['mode']:
    #             lst1.append(i)
    #     lst=lst1
    if mode:
        lst=[
        i  for i in lst if i['mode']==mode
        ]
    if category:
        lst=[
            i for i in lst if i['category'] ==category
        ]
    
    return lst

@app.get('/courses/{course_id}')
def get_course(course_id: int):
    for i in courses:
        if i['id'] ==course_id:
            return i
    
    return {
        'message': ' k tim thay khoa hoc'
    }
    
    

