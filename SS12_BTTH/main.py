from database import *
from models import * 
from schemas import *
from UserService import *
from fastapi import HTTPException,status,FastAPI,Depends
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app=FastAPI()

@app.get('/documents',response_model=list[DocumentResponse],status_code=status.HTTP_200_OK)
def read_document(db:Session=Depends(get_db)):
    return get_document(db)

@app.post('/documents',response_model=DocumentResponse,status_code=status.HTTP_201_CREATED)
def add_document_1(doc:DocumentCreate,db:Session=Depends(get_db)):
    return add_document(doc,db)

@app.delete('/documents/{document_id}',status_code=status.HTTP_200_OK)
def del_document_1(document_id:int,db:Session=Depends(get_db)):
    check=del_document(document_id,db)
    if check == 1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='k tim thay id'
        )
    return{
        'message':f'da xoa thanh cong ng dung co id {document_id}'
    }

