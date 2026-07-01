from fastapi import FastAPI,HTTPException
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

#  example : 
# examples: [] lay dc nhieu vi du
#

class Students(BaseModel):
    fullname: str = Field(...,min_length=3,examples= ['lai trung lam'])
    email:EmailStr
    age: int = None
    course: str=None
    phone : str=None





@app.post('/students')
def add_student(student:Students):
    for i in data:
        if student.email ==i['email']:
            raise HTTPException(
                status_code=409,
                detail='email bi trung'
            )
        
    data.append(student.model_dump())

    return {
        'message':'da them thanh cong',
        'data':student
    }






