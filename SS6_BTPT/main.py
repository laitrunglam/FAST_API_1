from fastapi import FastAPI,HTTPException,status

app=FastAPI()

orders_list = {
    1: {"id": 1, "code": "SP001", "payment_status": "PAID", "method": "BANK_TRANSFER"},
    2: {"id": 2, "code": "SP002", "payment_status": "UNPAID", "method": "NONE"}
}



@app.get('/orders/{order_id}/payment',status_code=status.HTTP_200_OK)
def get_order(order_id:int):
    try:
        product=orders_list.get(order_id)
        if not product:
            raise HTTPException(
                status_code= status.HTTP_404_NOT_FOUND,
                detail='ma k ton tai'
            )
        return {
            'payment_status' : product['payment_status'],
            'method': product['method']
        }
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='he thong hien tai dang loi vui long thu lai'
        )
    


