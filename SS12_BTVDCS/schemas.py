from pydantic import BaseModel,Field

class ShipmentUpdate(BaseModel):
    receiver_name: str
    delivery_address: str

class ShipmentRespone(BaseModel):
    id:int
    tracking_code: str
    receiver_name: str
    delivery_address: str

    class Config():
        from_attributes=True

class message(BaseModel):
    mess: str = Field(default='chuc mung ban da them thanh cong')
    data: ShipmentRespone


