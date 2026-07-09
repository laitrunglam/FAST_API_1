from database import *
from models import *
from UserService import *
from schemas import *

from fastapi import FastAPI,HTTPException,status,Depends
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app =FastAPI()

@app.get('/documents',response_model=list[DocumentRespone],status_code= status.HTTP_200_OK)
def get_all_documet(db:Session=Depends(get_db)):
    return get_all(db)

@app.post('/documents',response_model=DocumentRespone,status_code=status.HTTP_201_CREATED)
def post_document(doc:DocumentCreate, db: Session=Depends(get_db)):
    return add_document(doc,db)


@app.delete('/documents/{document_id}',status_code=status.HTTP_200_OK)
def delete_document(document_id: int, db:Session=Depends(get_db)):
    check = del_document(document_id,db)
    if check == 1:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail='k tim thay id'
        )
    
    return {
        'message':'da xoa thanh cong',
        'data':check
    }


