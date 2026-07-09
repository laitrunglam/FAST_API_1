from models import InventoryModel
from schemas import InvetoryCreate
from sqlalchemy.orm import Session


def check(inventory: InvetoryCreate,db:Session):
    is_flag= db.query(InventoryModel).filter(InventoryModel.warehouse_code== inventory.warehouse_code).first()
    if is_flag is not None:
        return 1
    
    new_invetory= InventoryModel(warehouse_code=inventory.warehouse_code,location=inventory.location)
    db.add(new_invetory)
    db.commit()
    db.refresh(new_invetory)

    return new_invetory

