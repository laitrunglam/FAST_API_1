from fastapi import FastAPI

letienthinh=FastAPI(
    title='Xử lý danh sách sách theo trạng thái',
    description='api tra ve danh sach khoa hoc'
)

course=[
  {
    "id": 1,
    "title": "Python Basic",
    "author": "Nguyen Van A",
    "category": "programming",
    "year": 2022,
    "is_available": True

  },
  {
    "id": 2,
    "title": "Python Medium",
    "author": "Nguyen Van B",
    "category": "programming",
    "year": 2023,
    "is_available": False
  },
]

@letienthinh.get('/books/available')
def get_books_available():
    lst=[]
    for i in course:
        if i['is_available'] is True:
            lst.append(i)
    return lst

@letienthinh.get('/books/borrowed')
def get_books_borrow():
    lst=[]
    for i in course:
        if i['is_available'] is False:
            lst.append(i)
    return lst