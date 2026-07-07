from fastapi import FastAPI,HTTPException,status,Depends
from sqlalchemy.orm import Session

from database import *
from models import *
from schemas import *
from UserService import *

app=FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db=LocalSession()
    try:
        yield db
    finally:
        db.close()

@app.post('/shipments',response_model=ShipmentRespone,status_code=status.HTTP_201_CREATED)
def add_shipment(ship:ShipmentCreate,db:Session=Depends(get_db)):
    check =create_shipment(ship,db)
    if check is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Mã vận đơn này đã được khởi tạo trước đó'
        )
    return check


@app.get('/shipments',response_model=list[ShipmentRespone],status_code=status.HTTP_200_OK)
def get_all(db:Session=Depends(get_db)):
    return get_all_shipmet(db)
    

@app.get('/shipments/{shipment_id}',response_model=ShipmentRespone,status_code=status.HTTP_200_OK)
def get_shipment_id(shipment_id: int, db:Session=Depends(get_db)):
    check=get_shiment_id(shipment_id,db)
    if check is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='k tim thay'
        )
    return check
    