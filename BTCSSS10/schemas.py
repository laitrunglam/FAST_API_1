from pydantic import BaseModel

#  mục địch file này là nhận dữ liệu đầu vào và trả được dữ liệu đầu ra.

#  dữ liệu đầu vào ng dùng 
class InvetoryCreate(BaseModel):
    warehouse_code:str
    location: str

#  dữ liệu đầu ra mong muốn
class InvetoryRespone(BaseModel):
    id:int
    warehouse_code: str
    location: str

    # class Config():
    #     orm_mode=True