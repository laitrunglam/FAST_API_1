from models import Document
from schemas import DocumentCreate
from sqlalchemy.orm import Session

def get_document(db:Session):
    return db.query(Document).all()

def add_document(doc: DocumentCreate,db:Session):
    new_doc=Document(
        title= doc.title,
        subject=doc.subject,
        document_type=doc.document_type,
        file_url=doc.file_url
    )

    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)

    return new_doc

def del_document(document_id,db:Session):
    check=db.query(Document).filter(document_id==Document.id).first()
    if check is None:
        return 1
    db.delete(check)
    db.commit()
    return 0
    