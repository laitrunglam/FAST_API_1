# from fastapi import FastAPI,HTTPException,status
# from pydantic import BaseModel,Field,field_validator

from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel,Field

app=FastAPI()

products = [
    {"id": 1, "name": "Keyboard", "price": 500000},
    {"id": 2, "name": "Mouse", "price": 300000}
]

class Products(BaseModel):
    name: str =Field(...,min_length=1)
    price: float =Field(...,ge=0)

@app.post('/products',status_code=status.HTTP_201_CREATED)
def get_products(product:Products):
    id_new=products[len(products)-1]['id']+1
    new_product={
        "id": id_new, "name": product.name, "price": product.price
    }

    products.append(new_product)
    return {
        'message':'them san pham thanh cong',
        'data':new_product
    }

    


@app.get('/products')
def get_ds():
    return products

@app.delete('/products/{product_id}')
def del_product(product_id:int):
    for i in products:
        if product_id==i['id']:
            products.remove(i)
            return {
                'message':f'da xoa thanh cong san pham co ma {product_id}'
            }
    raise HTTPException(
        status =404,
        detail= "Product not found"
    )



    
        


    