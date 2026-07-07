from fastapi import FastAPI,Query,HTTPException
from typing import Optional

app=FastAPI()

products = [
    {"id": 1, "name": "Laptop", "price": 15000000},
    {"id": 2, "name": "Mouse", "price": 200000},
    {"id": 3, "name": "Keyboard", "price": 500000},
    {"id": 4, "name": "Monitor", "price": 3000000}
]

@app.get('/products')
def get_product(
    keyword : Optional[str] = Query(None,description='Tìm sản phẩm theo tên'),
    max_price: Optional[float] = Query(None,description='Lọc sản phẩm có giá nhỏ hơn hoặc bằng giá này')
):
    if max_price is not None  :
        if max_price<0:
            raise HTTPException(
                status_code=400,
                detail='max price k dc nho hon 0'
            )
    
    lst=products
    
    if keyword:
        lst=[
            i for i in lst if keyword.lower() in i['name'].lower()
        ]

    if max_price:
        lst=[
            i for i in lst if i['price']<=max_price
        ]

    return lst
    

