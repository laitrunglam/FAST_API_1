from pydantic import BaseModel

class ShipmentCreate(BaseModel):
    tracking_number: str

class ShipmentRespone(BaseModel):
    id: int
    tracking_number: str
    status: str

    class config():
        from_attributes=True
        

    