from fastapi import FastAPI

app=FastAPI(
    title='Thống kê dữ liệu sách trong thư viện',
    description='quan ly api cho du lieu sach'
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
    "category": "database",
    "year": 2023,
    "is_available": False
  },
  {
    "id": 3,
    "title": "Hard",
    "author": "Nguyen Van C",
    "category": "web",
    "year": 2026,
    "is_available": False
  },
   {
    "id": 4,
    "title": "Hard",
    "author": "Nguyen Van C",
    "category": "web",
    "year": 2026,
    "is_available": False
  },
]

@app.get('/books/statistics')
def get_statistics():
    available_books=0
    borrowed_books=0
    for i in course:
        if i['is_available'] is True:
            available_books+=1
        else:
            borrowed_books+=1
    
    return {
    "total_books": len(course),
    "available_books": available_books,
    "borrowed_books": borrowed_books
    }



@app.get('/books/categories')
def get_categories():
    lst=[]
    for i in course:
        if i['category'] not in lst:
            lst.append(i['category'])
    return lst

@app.get('/books/latest')
def get_year_max():
    if not course:
        return {
            "message": "No books available"
        }
    max=course[0]
    for i in course:
        if max['year'] <i['year']:
            max=i

    return {
        'message': max
    }

@app.get('/books/sort')
def get_sort_book():
    lst=[]
    lst=sorted(course,key=lambda x: x['year'])
    return lst[::-1]
