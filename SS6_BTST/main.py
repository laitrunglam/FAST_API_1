from fastapi import FastAPI,HTTPException,status,Request
from fastapi.exceptions import RequestValidationError
from datetime import datetime
from fastapi.responses import JSONResponse
from typing import Any


app=FastAPI()
# Any nghia la mk chua biet ro mang kieu du lieu j( Nho import thu vien)
def respone_json( statusCode: int , message: str, data : Any, error : Any,  path: str):
    return JSONResponse(
        status_code= statusCode,
        content={
            "statusCode" : statusCode,
            "message" : message,
            "data" : data,
            'error': error,
            "timestamp": datetime.now().isoformat() ,
            "path": path
        }
    )
#  tanafg 1 loi do ng dung 
@app.exception_handler(RequestValidationError)
def exception_validate(request : Request, req:RequestValidationError):
    return respone_json(
        statusCode= 422,
        message= ' loi do ng dung',
        data= None,
        error=req.errors(),
        path=request.url.path
    )

#  tang 2 : loi do develope tu dinh nghia
@app.exception_handler(HTTPException)
def execption_http(reques: Request, exc:HTTPException):
    return respone_json(
        statusCode= exc.status_code,
        message=exc.detail,
        data= None,
        error=exc.detail,
        path=reques.url.path
    )

#  tang 3: loi con lai do he thong 
@app.exception_handler(Exception)
def exception_Exception(request: Request,e:Exception):
    return respone_json(
        statusCode=500,
        message='loi do server',
        data= None,
        error= str(e),
        path=request.url.path
    )

orders_db = [
    {"id": 1, "code": "SP001", "status": "PENDING"},
    {"id": 2, "code": "SP002", "status": "DELIVERED"}
]

@app.delete('/orders/{order_id}',status_code=status.HTTP_200_OK)
def del_order_id(order_id: int,request: Request):
    is_flag=None
    for i in orders_db:
        if i['id']  == order_id:
            is_flag =i
            break
    if is_flag is None:
        raise HTTPException(
            status_code= 404,
            detail='loi k tim thay id'
        )
    
    if is_flag['status'] == 'DELIVERED':
        raise HTTPException(
            status_code= 400,
            detail='k dc phep huy'
        )
    
    is_flag['status'] ='CANCELLED'

    return respone_json(
        statusCode= 200,
        message='da thay doi trang thai thanh cong',
        data= is_flag,
        error= None,
        path=request.url.path
    )

    
   



