from sqlalchemy.orm import Session
from models import DiscountModel
from datetime import datetime

def delete_discount_service(db: Session, discount_id: int):
    # 1. Tìm kiếm mã giảm giá theo discount_id và chưa bị xóa trước đó
    discount = db.query(DiscountModel).filter(
        DiscountModel.id == discount_id,
        DiscountModel.is_deleted == False
    ).first()
    
   
    if discount is None:
        return "NOT_FOUND"
        
    if discount.is_active:
        return "CODE_IS_ACTIVE"
        
    
    discount.is_deleted = True
    discount.deleted_at = datetime.now()
    
    db.commit()
    db.refresh(discount)
    
    return discount