from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

url_database = 'mysql+pymysql://root:21122003@localhost:3306/ecommerce_db'

engine=create_engine(url_database)

LocalSession=sessionmaker(autoflush= False, autocommit=False,bind=engine)

Base = declarative_base()

def get_db():
    db=LocalSession()
    try:
        yield db
    finally:
        db.close()

