from database import Base
from  sqlalchemy import Column,String,Integer


class Document(Base):
    __tablename__ = 'documents'

    id = Column(Integer,primary_key= True)
    title = Column(String(50), nullable= False)
    subject= Column(String(50),nullable= False)
    document_type= Column(String(50),nullable= False)
    file_url=Column(String(50),nullable= False)