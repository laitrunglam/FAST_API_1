from models import ShipmentModel
from schemas import ShipmentCreate
from sqlalchemy.orm import Session

def create_shipment(ship:ShipmentCreate,db:Session):
    check = db.query(ShipmentModel).filter(ShipmentModel.tracking_number==ship.tracking_number).first()
    if check:
        return None
    new_shipment=ShipmentModel(tracking_number=ship.tracking_number)
    db.add(new_shipment)
    db.commit()
    db.refresh(new_shipment)

    return new_shipment

def get_all_shipmet(db:Session):
    return db.query(ShipmentModel).all()


    
def get_shiment_id(shipment_id: int,db:Session):
    # database = db.query(ShipmentModel).all()
    # for i in database:
    #     if i.id==shipment_id:
    #         return i
    
    # return None

    check= db.query(ShipmentModel).filter(ShipmentModel.id==shipment_id).first()
    
    return check
    
    