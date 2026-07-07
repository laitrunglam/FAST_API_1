from sqlalchemy import create_engine
from sqlalchemy.orm import  sessionmaker,declarative_base


url_db="mysql+pymysql://root:21122003@localhost:3306/crm_db"

engine= create_engine(url_db)

SessionLocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base=declarative_base()

