from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DiscountResponse(BaseModel):
    id: int
    code: str
    discount_value: int
    is_active: bool
    is_deleted: bool
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True 