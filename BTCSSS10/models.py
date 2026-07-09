from database import Base
from sqlalchemy import Column,Integer,String

#  file models dùng để tạo bảng trong sql workbench hay vì bọn em phải tạo tay.
#  nhớ phải import thằng Base từ file databse sang 

class InventoryModel(Base):
    __tablename__ = "inventories"
    id = Column(Integer, primary_key=True)
    warehouse_code = Column(String(50), unique=True, nullable=False) # Khóa duy nhất
    location = Column(String(100), nullable=False)