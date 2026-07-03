from fastapi import FastAPI, status, HTTPException,Request
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from datetime import datetime

app = FastAPI()

# Dữ liệu nội bộ trong bộ nhớ tạm
promo_codes_db = {
    "SUMMER25": {"code": "SUMMER25", "discount_rate": 0.15, "max_budget": 50000000, "is_active": True},
    "WELCOME50": {"code": "WELCOME50", "discount_rate": 0.50, "max_budget": 10000000, "is_active": False}
}

# Model nội bộ chứa cả trường ngân sách chiến dịch nhạy cảm (Cấm lộ)
class PromoInternal(BaseModel):
    code: str
    discount_rate: float
    max_budget: int # Trường nhạy cảm - Không được lộ ra Client!
    is_active: bool


class PromoPublic (BaseModel):
    code: str
    discount_rate: float

@app.get('/promos/{code})',response_model=PromoPublic,status_code=status.HTTP_200_OK)
def get_promo(code:str):
    if code not in promo_codes_db:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail='Mã giảm giá không tồn tại'
        )
    
    product=promo_codes_db[code]
    if product['is_active'] is False:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Mã giảm giá đã hết hạn sử dụng'
        )
    
    return  {
        'code':code,
        'discount_rate':product['discount_rate']
    }


@app.exception_handler(HTTPException)
def hanlde_execption(request: Request,exc:HTTPException):
    return JSONResponse(
        status_code= exc.status_code,
        content ={
            'statusCode': exc.status_code,
            'data': None,
            'erroer': 'client_error' if exc.status_code<500 else 'server error',
            'message': exc.detail,
            'timestamp': datetime.now().isoformat(),
            'path': request.url.path
        }
    )


