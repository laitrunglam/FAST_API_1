from pydantic import BaseModel

class MemberShipCreate(BaseModel):
    card_number: str
    customer_id: int

class MemberShipRespone(BaseModel):
    status: str
    message: str
    code: int
    data: dict | None
    error: str | None

    class Config:
        from_attributes = True