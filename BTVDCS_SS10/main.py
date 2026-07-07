from fastapi import FastAPI,status,HTTPException,Depends
from sqlalchemy.orm import Session

from database import engine,Sessionlocal,Base
from models import InventoryModel
from schemas import InvertoryCreate, InvertoryRespone


Base.metadata.create_all(bind=engine)

app=FastAPI()

def get_db():
    db=Sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/inventories',response_model=InvertoryRespone,status_code=status.HTTP_201_CREATED)
def create_invetory(invetory: InvertoryCreate,db:Session=Depends(get_db)):
    check_invetory=db.query(InventoryModel).filter(InventoryModel.warehouse_code==invetory.warehouse_code).first()
    if check_invetory:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Mã kho vận đã tồn tại trên hệ thống, không thể tạo trùng'
        )
    
    new_invetory=InventoryModel(
        warehouse_code= invetory.warehouse_code,
        location= invetory.location
    )

    db.add(new_invetory)
    db.commit()
    db.refresh(new_invetory)

    #  trả về 1 object chứ k phải dict nên phải dùng config
    return new_invetory
