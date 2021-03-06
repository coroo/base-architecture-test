from fastapi import Depends, APIRouter, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.schemas import item_schema
from app.deliveries import item_delivery
from app.middlewares import deps

router = APIRouter()

@router.post("/users/{user_id}/items/", response_model=item_schema.Item)
def create_item_for_user(
    user_id: int, item: item_schema.ItemCreate, db: Session = Depends(deps.get_db)
):
    return item_delivery.create_user_item(db=db, item=item, user_id=user_id)

@router.get("/items/", response_model=List[item_schema.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    items = item_delivery.get_items(db, skip=skip, limit=limit)
    return items