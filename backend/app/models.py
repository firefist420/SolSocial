from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Float, Boolean
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    wallet_address = Column(String(44), unique=True, index=True)
    username = Column(String(50), unique=True, nullable=True)
    bio = Column(Text, nullable=True)
    hashed_password = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    posts = relationship("Post", back_populates="author")
    tokens = relationship("Token", back_populates="creator")

class Token(Base):
    __tablename__ = "tokens"
    id = Column(Integer, primary_key=True, index=True)
    contract_address = Column(String(44), unique=True, index=True)
    name = Column(String(100))
    symbol = Column(String(10))
    description = Column(Text, nullable=True)
    website = Column(String(255), nullable=True)
    twitter = Column(String(255), nullable=True)
    telegram = Column(String(255), nullable=True)
    discord = Column(String(255), nullable=True)
    price = Column(Float, nullable=True)
    price_change_24h = Column(Float, nullable=True)
    liquidity = Column(Float, nullable=True)
    creator_wallet = Column(String(44), ForeignKey("users.wallet_address"))
    created_at = Column(DateTime, default=datetime.utcnow)
    creator = relationship("User", back_populates="tokens")

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
    author_wallet = Column(String(44), ForeignKey("users.wallet_address"))
    token_address = Column(String(44), ForeignKey("tokens.contract_address"), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    author = relationship("User", back_populates="posts")
    token = relationship("Token")