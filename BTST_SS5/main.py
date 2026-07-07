from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field

app=FastAPI()

products = [
    {"id": 1, "code": "SP001", "name": "Keyboard", "price": 500000, "is_active": True},
    {"id": 2, "code": "SP002", "name": "Mouse", "price": 300000, "is_active": True},
    {"id": 3, "code": "SP003", "name": "Monitor", "price": 2500000, "is_active": False}
]


@app.patch('/products/{product_id}')
def update_product(product_id:int ):
    is_check=None
    for i in products:
        if i['id']==product_id:
            is_check=i
            break
    if is_check is None:
        raise HTTPException(
            status_code=404,
            detail='Product not found'
        )
    if is_check['is_active'] is False:
        raise HTTPException(
            status_code=409,
            detail='Product already inactive'
        )
    else:
        is_check["is_active"] = False
    
    return{
        'message': 'ngung kinh doanh thanh cong'
    }


            

    
    
