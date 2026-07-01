from fastapi import FastAPI,status
from pydantic import BaseModel,Field,EmailStr,field_validator

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

app=FastAPI()
class Students(BaseModel):
    full_name: str =Field(...,min_length=3,examples=['luong quoc tuan'])
    email: EmailStr
    age: int =Field(...,ge=15,le=60,examples=[40])
    phone: str =Field(...,min_length=10,max_length=11,examples=['0913367524'])
    course: str
    note: str=Field(None,max_length=200)

    @field_validator('phone')
    def check(phone):
        if not phone.isdigit():
            raise ValueError('k dc nhap chu')
        return phone
    
@app.post('/students/register',status_code=status.HTTP_201_CREATED)
def add_student(student:Students):
    return student