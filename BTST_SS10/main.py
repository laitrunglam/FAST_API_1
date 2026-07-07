from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import Base, engine, SessionLocal
from models import CustomerModel, MembershipModel
from schemas import MembershipCreate, MembershipResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/memberships", response_model=MembershipResponse)
def create_membership(
    payload: MembershipCreate,
    db: Session = Depends(get_db)
):

    customer = (
        db.query(CustomerModel)
        .filter(CustomerModel.id == payload.customer_id)
        .first()
    )

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Khách hàng không tồn tại trên hệ thống"
        )

  
    existing_card = (
        db.query(MembershipModel)
        .filter(MembershipModel.card_number == payload.card_number)
        .first()
    )

    if existing_card:
        raise HTTPException(
            status_code=400,
            detail="Mã số thẻ thành viên này đã được sử dụng"
        )

   
    new_membership = MembershipModel(
        card_number=payload.card_number,
        customer_id=payload.customer_id
    )

    db.add(new_membership)
    db.commit()
    db.refresh(new_membership)

    return {
        "status": "success",
        "message": "Tạo thẻ thành viên thành công",
        "code": 201,
        "data": {
            "id": new_membership.id,
            "card_number": new_membership.card_number,
            "customer_id": new_membership.customer_id
        },
        "error": None
    }