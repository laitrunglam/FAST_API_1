from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel,Field,EmailStr

app=FastAPI()

data=[
    {
  "full_name": "Nguyen Van A",
  "email": "vana@gmail.com",
  "age": 20,
  "course": "python",
  "phone": "0987654321"
}
]

# example , examples, json_schema_extra

class Students(BaseModel):
    full_name: str =Field(...,min_length=3,examples=['lai trung lam'])
    email:EmailStr
    age: int = Field(...,examples=[20])
    course: str
    phone: str


@app.post('/students')
def add_students(student: Students):
    for i in data:
        if i['email'] == student.email:
            raise HTTPException(
                status_code= 409,
                detail='trung email'
            )
    data.append(student.model_dump())
    return student





