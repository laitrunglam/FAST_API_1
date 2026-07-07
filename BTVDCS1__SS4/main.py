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
    keyword: Optional[str]=Query(None,description='Tìm sản phẩm theo tên'),
    max_price: Optional[float]=Query(None,description='Lọc sản phẩm có giá nhỏ hơn hoặc bằng giá này')
):
    if  max_price is not None and max_price<0 :
        raise HTTPException(
            status_code=400,
            detail='max_price không được âm'
        )
    
    lst=products

    if keyword:
        lst=[
            c for c in lst if keyword.lower() in c['name'].lower()
        ]
    
    if max_price:
        lst=[
            c for c in lst if max_price>=c['price']
        ]
    
    return {
        'message':'da tim thay san pham',
        'data':lst
    }


    
    