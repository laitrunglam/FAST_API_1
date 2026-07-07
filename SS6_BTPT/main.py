from fastapi import FastAPI,status,HTTPException

app=FastAPI()


orders_list = {
    1 :{"id": 1, "code": "SP001", "payment_status": "PAID", "method": "BANK_TRANSFER"},
    2 :{"id": 2, "code": "SP002", "payment_status": "UNPAID", "method": "NONE"}
}



@app.get('/orders/{order_id}/payment',status_code=status.HTTP_200_OK)
def get_order(order_id:int):
    try:
        # dung get de tranh lam crash chuong trinh neu k ton tai order_id
        product=orders_list.get(order_id)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='k tim thay id'
            )
        return{
            'payment_status': product['payment_status'],
            'method': product['method']
        }
    except HTTPException  :
        raise 
    except Exception as e:
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail= f'loi do server {e}'
        )
 