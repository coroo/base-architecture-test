from sqlalchemy.orm import Session

from app.models import item_model
from app.schemas import item_schema


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(item_model.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: item_schema.ItemCreate, user_id: int):
    db_item = item_model.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item