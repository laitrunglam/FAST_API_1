from fastapi import FastAPI,Request,HTTPException,status
from fastapi.responses import JSONResponse
from datetime import datetime
from fastapi.exceptions import RequestValidationError
from typing import Any


app=FastAPI()

orders_db = [
    {"id": 1, "code": "SP001", "status": "PENDING"},
    {"id": 2, "code": "SP002", "status": "DELIVERED"}
]


def envelope(status_code: int, message: str,data: any, error: str,path: str):
    return JSONResponse(
        status_code= status_code,
        content={
            'statusCode': status_code,
            'message': message,
            'data': data,
            'error': error,
            'timestamp': datetime.now().isoformat(),
            'path':path
        }
    )

@app.exception_handler(RequestValidationError)
def validate_request(request: Request, exc:RequestValidationError):
    return envelope(
        status_code= status.HTTP_422_UNPROCESSABLE_CONTENT,
        message= 'INVALID CONTENT',
        data= None,
        error=exc.errors(),
        path=request.url.path
    )


@app.exception_handler(HTTPException)
def hanlde_http_exception(request: Request,exc:HTTPException):
    return envelope(
        status_code=exc.status_code,
        message=exc.detail,
        data=None,
        error=exc.detail,
        path=request.url.path
    )

@app.exception_handler(Exception)
def hanlde_exception(request: Request,exc:Exception):
    return envelope(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        message='loi he thong vui long thu lai sau',
        data=None,
        error=exc,
        path=request.url.path
    )

@app.delete('/orders/{order_id}',status_code=status.HTTP_202_ACCEPTED)
def add_order(order_id: int, request:Request):
    is_flag=None
    for i in orders_db:
        if i['id'] ==order_id:
            is_flag=i
    if is_flag is None:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail='ID k ton tai'
        )
    
    if is_flag['status'] =='DELIVERED':
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='he thong k cho phep huy'
        )
    
    is_flag['status']='CANCELLED'

    return envelope(
        status_code=200,
        message='da thay doi trang thai thanh cong',
        data= is_flag,
        error= None,
        path=request.url.path
    )
