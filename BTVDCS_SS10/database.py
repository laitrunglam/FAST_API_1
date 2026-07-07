from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

url_database='mysql+pymysql://root:21122003@localhost:3306/ecommerce_db'

#  khoi tao 1 dong co ket noi engine.moi khi api can doc ghi du lieu, engine se cap ra 1 ket noi, xly xong lai thu hoi
engine=create_engine(url_database)
"""
- tao ra 1 nha may de duc ra cac phien lam viec
-autocommit=false: tat che ong tu dong luu
-autoflush=fasle: tat che do tu dong dong bo tam thoi
"""
Sessionlocal = sessionmaker(autoflush= False,autocommit=False,bind=engine)

"""
khoi tao 1 lop co so basemodel cho cac model orm
Sau câu lệnh này, bất kỳ bảng dữ liệu nào bạn muốn tạo ra trong mã nguồn (ví dụ: class InventoryModel(Base): ) 
đều phải kế thừa từ cục Base này. Nó đóng vai trò làm "trung gian", 
định hình và đăng ký cấu trúc các class Python để SQLAlchemy hiểu và tự động ánh xạ (map) thành các bảng tương ứng dưới MySQL.
"""
Base=declarative_base()


