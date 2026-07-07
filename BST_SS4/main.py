from fastapi import FastAPI,status
from pydantic import BaseModel,Field,EmailStr,field_validator

app=FastAPI()

data=[
    {
  "full_name": "Nguyen Van A",
  "email": "vana@example.com",
  "age": 20,
  "phone": "0987654321",
  "course": "python",
  "note": "Muon hoc lop buoi toi"
}
]
class Students(BaseModel):
    full_name : str = Field(...,min_length=3,examples=['lai trung lam'])
    email: EmailStr
    age: int =Field(..., ge=15,le=60,examples=[40] )
    phone : str =Field(...,min_length=10,max_length=11,examples=['0855582835'])
    course: str
    note: str=Field(None,max_length=200,examples=['duong vibe coding'])

    @field_validator('phone')
    def check(phone):
        if not phone.isdigit():
            raise ValueError('sai dinh dang')
    
        return phone


@app.post('/students/register',status_code=status.HTTP_201_CREATED)
def add_student(student: Students):
    data.append(student.model_dump())
    return {
        'message':'da them thanh cong',
        'data': student
    }



