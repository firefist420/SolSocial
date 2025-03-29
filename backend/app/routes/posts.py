from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import PostCreate, Post
from ..crud import create_post, get_posts
from ..auth import get_current_user
from .. import models

router = APIRouter(prefix="/posts", tags=["posts"])

@router.post("/", response_model=Post)
def create_new_post(
    post: PostCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return create_post(db, post, current_user.wallet_address)

@router.get("/", response_model=list[Post])
def read_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_posts(db, skip=skip, limit=limit)