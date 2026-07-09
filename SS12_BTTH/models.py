from sqlalchemy import Column,String,Integer
from database import Base

class Document(Base):
    __tablename__ = 'Documents'
    id = Column(Integer,primary_key=True)
    title=Column(String(255),nullable= False)
    subject=Column(String(50),nullable= False)
    document_type=Column(String(50),nullable= False)
    file_url=Column(String(50),nullable=False)

