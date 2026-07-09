from fastapi import FastAPI, Depends, status,HTTPException
from sqlalchemy.orm import Session

from models import * 
from schemas import *
from serivces import *
from database import *

app = FastAPI(title="Shipment Management System")

Base.metadata.create_all(bind=engine)

@app.put('/shipments/{shipment_id}',response_model=message,status_code=status.HTTP_200_OK)
def update_shipment(shipment_id:int, shipment_update: ShipmentUpdate,db:Session=Depends(get_db)):
    check= update_shipment_service(db,shipment_id,shipment_update)
    if check==1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='k tim thay id'
        )
    
    
    return {
        'mess': ' da them thanh cong',
        'data': check
    }
