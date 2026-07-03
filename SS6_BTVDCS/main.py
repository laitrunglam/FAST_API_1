from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel

class Product(BaseModel):
    id: int
    quantity: int

app=FastAPI()


products_db = [
    {"id": 101, "name": "Bàn phím cơ", "stock": 5, "price": 1200000.0},
    {"id": 102, "name": "Chuột Gaming", "stock": 2, "price": 600000.0}
]
orders_db = []


@app.post('/orders',status_code=status.HTTP_201_CREATED)
def add_order(product:Product):
    is_flag=None
    for i in products_db:
        if product.id == i['id']:
            is_flag=i
            break
    
    if is_flag is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='k tim thay id trong kho'
        )
    

    if product.quantity<=0:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail='so luong mua k dc nho hon bang 0'
        )
    
    if product.quantity> is_flag['stock']:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='so luong mua k dc lon hon ton kho'
        )
    
    is_flag['stock']-=product.quantity
    
    new_product = {
        'id' : len(orders_db)+1,
        'product_id' : product.id,
        'name': is_flag['name'],
        'quantity': product.quantity,
        'price': is_flag['price']*product.quantity
    }

    orders_db.append(new_product)
    return{
        'message':'da them don hang thanh cong',
        'data': new_product
    }


@app.get('/course')
def get_course():
    return orders_db
