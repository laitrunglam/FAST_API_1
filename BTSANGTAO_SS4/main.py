from fastapi import FastAPI,status
from pydantic import BaseModel,Field,EmailStr,field_validator

app=FastAPI()

class Students(BaseModel):
    fullname:str=Field(...,min_length=3,examples=['LAI TRUNG LAM'])
    email:EmailStr
    age: int =Field(...,ge=15,le=60,examples=[20])
    phone: str=Field(...,min_length=10,max_length=11,examples=['0855582736'])
    course:str
    note: str=Field(None,max_length=200)

    @field_validator('phone')
    def validate(phone):
        if not phone.isdigit():
            raise ValueError('sai dinh dang')
        
        return phone
    
@app.post('/students/register',status_code=status.HTTP_201_CREATED)
def register_student(student:Students):
        return {
             'message':'Đăng ký học viên thành công',
             'data':student
        }

