from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from database import Base

class DiscountModel(Base):
    __tablename__ = "discounts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(String(50), unique=True, nullable=False)
    discount_value = Column(Integer, nullable=False) # Phần trăm hoặc số tiền giảm
    

    is_active = Column(Boolean, default=True, nullable=False) # Trạng thái hoạt động
    is_deleted = Column(Boolean, default=False, nullable=False) # Đánh dấu xóa mềm
    deleted_at = Column(DateTime, nullable=True) # Thời điểm thực hiện xóa mềm