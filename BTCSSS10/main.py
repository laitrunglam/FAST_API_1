from database import *
from models import *
from schemas import *
from UserService import *

from fastapi import FastAPI,HTTPException,status,Depends
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app=FastAPI()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/addStudent',response_model=InvetoryRespone,status_code=status.HTTP_201_CREATED)
def add_student(invetory:InvetoryCreate,db:Session=Depends(get_db)):
    is_flag=check(invetory,db)
    if is_flag == 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='ma loi bi trung'
        )
    
    return is_flag

