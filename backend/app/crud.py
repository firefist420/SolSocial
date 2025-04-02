from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime

def get_user(db: Session, wallet_address: str):
    return db.query(models.User).filter(models.User.wallet_address == wallet_address).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, wallet_address: str, user_update: schemas.UserUpdate):
    db_user = get_user(db, wallet_address)
    if db_user:
        update_data = user_update.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_user, field, value)
        db.commit()
        db.refresh(db_user)
    return db_user

def get_token(db: Session, token_id: int):
    return db.query(models.Token).filter(models.Token.id == token_id).first()

def get_token_by_contract(db: Session, contract_address: str):
    return db.query(models.Token).filter(models.Token.contract_address == contract_address).first()

def get_tokens(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Token).offset(skip).limit(limit).all()

def create_token(db: Session, token: schemas.TokenCreate, creator_wallet: str):
    db_token = models.Token(**token.dict(), creator_wallet=creator_wallet)
    db.add(db_token)
    db.commit()
    db.refresh(db_token)
    return db_token

def update_token(db: Session, token_id: int, token_update: schemas.TokenUpdate):
    db_token = get_token(db, token_id)
    if db_token:
        update_data = token_update.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_token, field, value)
        db.commit()
        db.refresh(db_token)
    return db_token

def get_post(db: Session, post_id: int):
    return db.query(models.Post).filter(models.Post.id == post_id).first()

def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Post).offset(skip).limit(limit).all()

def create_post(db: Session, post: schemas.PostCreate, author_wallet: str):
    db_post = models.Post(**post.dict(), author_wallet=author_wallet)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post