from models import ShipmentModel
from sqlalchemy.orm import Session
from schemas import ShipmentUpdate

def update_shipment_service(db:Session, shipment_id:int, shipment_update: ShipmentUpdate):
    check = db.query(ShipmentModel).filter(shipment_id==ShipmentModel.id).first()
    if check is None:
        return 1
    
    check.receiver_name= shipment_update.receiver_name
    check.delivery_address=shipment_update.delivery_address

    db.commit()
    db.refresh(check)

    return    check
