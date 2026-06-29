from fastapi import FastAPI,HTTPException

app=FastAPI(
    title='Mini API danh sách khóa học với FastAPI',
    description='quan ly api danh sach khoa hoc'
)   

courses = [
    {
        "id": 1,
        "code": "PY101",
        "name": "Python Basic",
        "level": "beginner",
        "price": 1500000
    },
    {
        "id": 2,
        "code": "FA101",
        "name": "FastAPI Basic",
        "level": "beginner",
        "price": 2000000
    }
]


@app.get('//health')
def get_loichao():
    return {
        "message": "API is running"
    }



@app.get('/courses')
def get_ds_kh():
    return courses

@app.get('/courses/{course_id}')
def get_course_id(course_id : int):
    if course_id<0:
        raise HTTPException(
            status_code=400,
            detail='course id khong dc nho hon 0'
        )
    
    for i in courses:
        if course_id == i['id']:
            return {
                'message':i,
                
            }
    else:
        raise HTTPException(
            status_code=404,
            detail='loi k tim thay k hoa'
        )

    
    