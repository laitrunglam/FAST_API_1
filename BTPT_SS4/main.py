from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field,EmailStr
from typing import Optional

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

class Students(BaseModel):
    fullname: str = Field(...,min_length=3,examples=['lai trung lam','luong quoc tuan'])
    email:EmailStr 
    age: Optional[int] =Field(...,examples=[20])
    course: Optional[str]
    phone:str


@app.post('/students')
def add_student(student: Students):
    for i in data:
        if i['email']==student.email:
            raise HTTPException(
                status_code= 409,
                detail='email bi trung'
            )
    data.append(student.model_dump())
    return   student
    
