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
def get_kh():
    return {
         "message": "Lấy danh sách khóa học thành công",
         'data':  courses
    }

@app.get('/courses/search')
def search_course(
    mode: Optional[str]=Query(None,description='Lọc theo hình thức học: online/offline') ,
    category: Optional[str] = Query(None,description='Lọc theo nhóm khóa học: backend/fe')
):
    lst=courses
    # if mode:
    #     lst1=[]
    #     for i in lst:
    #         if i['mode'] ==mode:
    #             lst1.append(i)
    #     lst=lst1
    
    if mode:
        lst=[
            c for c in lst if c['mode']==mode
        ]
    
    if category:
        lst=[
            c for c in lst if c['category']==category
        ]
    
    

    # if category:
    #     lst2=[]
    #     for i in lst:
    #         if i['category']==category:
    #             lst2.append(i)
    #     lst=lst2
    
    return {
        'message':'loc thanh cong',
        'data': lst
    }
    

            
    
@app.get('/courses/{course_id}')
def get_course(course_id : int):
    
    for i in courses:
        if course_id ==i['id']:
            return {
                'mesaage':'da tim thay khoa hoc',
                'data':i
            }
            
        
    return {
        'message':'k tim thay khoa hoc'
    }




