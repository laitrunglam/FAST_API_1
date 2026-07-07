from pydantic import BaseModel

class InvertoryCreate(BaseModel):
    warehouse_code: str
    location: str

#  quy định API sẽ trả về những trường nào.
class InvertoryRespone(BaseModel):
    id: int
    warehouse_code: str
    location: str
# cho phép Pydantic đọc dữ liệu từ các thuộc tính của object (ví dụ new_inventory.id) 
# thay vì chỉ đọc từ dictionary. Đây là lý do nó thường xuất hiện khi dùng SQLAlchemy ORM.
    class config: 
        from_attributes = True
