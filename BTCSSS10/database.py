from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

#  url kết nối tới database
url_database='mysql+pymysql://root:21122003@localhost:3306/ecommerce_db'

# cầu nối thật sự 
engine=create_engine(url_database)

#  tao phien lafm viec moi lan ng dung gui request
SessionLocal = sessionmaker(autoflush=False,autocommit = False,bind=engine)

Base =declarative_base()

