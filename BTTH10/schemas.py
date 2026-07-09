from pydantic import BaseModel

class DocumentCreate(BaseModel):
    title : str
    subject: str
    document_type: str
    file_url: str

class DocumentRespone(BaseModel):
    id:int
    title : str
    subject: str
    document_type: str
    file_url: str

    class config():
        from_attributes=True
