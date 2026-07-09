from models import Document
from schemas import DocumentCreate
from sqlalchemy.orm import Session

def get_all(db:Session):
    check= db.query(Document).all()
    return check

def add_document(doc:DocumentCreate, db: Session):
    new_documnet= Document(
        title= doc.title,
        subject=doc.subject,
        document_type=doc.document_type,
        file_url=doc.file_url
    )
    db.add(new_documnet)
    db.commit()
    db.refresh(new_documnet)

    return new_documnet


def del_document(document_id: int, db:Session):
    check = db.query(Document).filter(document_id==Document.id).first()
    if check is None:
        return 1
    
    db.delete(check)
    db.commit()

    return check
