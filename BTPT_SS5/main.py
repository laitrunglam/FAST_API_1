from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel,Field

app=FastAPI()

products = [
    {"id": 1, "code": "SP001", "name": "Keyboard", "price": 500000, "stock": 10},
    {"id": 2, "code": "SP002", "name": "Mouse", "price": 300000, "stock": 5}
]

class Products(BaseModel):
    code: str =Field(...,examples=['SP003'])
    name: str =Field(...,examples=['IPAD'])
    price: int = Field(...,ge=1,examples=[20000])
    stock: int = Field(...,ge=0,examples=[11])


@app.put('/products/{product_id}',status_code= status.HTTP_202_ACCEPTED)
def update_product(product_id: int, product: Products):
    is_flag=None
    if product_id: 
        for i in products:
            if product_id == i['id']:
                is_flag=i
                break
    if is_flag is None:
        raise HTTPException(
            status_code=404,
            detail='product not found'
        )
    

    for i in products:
        if i['code']==product.code and i['id']!=product_id:
            raise HTTPException(
                status_code=409,
                detail='prouct is conflict'
            )

    is_flag.update(product.model_dump())

    return {
        'messagge':'da cap nhat thanh cong',
        'data': is_flag
    }

    

        
    





