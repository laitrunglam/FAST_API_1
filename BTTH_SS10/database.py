from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL = "mysql+pymysql://root:21122003@localhost:3306/ecommerce_db"

engine=create_engine(DATABASE_URL)

LocalSession=sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base=declarative_base()

