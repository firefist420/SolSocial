from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class WalletAuthRequest(BaseModel):
    wallet_address: str = Field(..., min_length=32, max_length=44)
    signed_message: List[int]
    message: str = Field(..., min_length=10)

class TokenData(BaseModel):
    wallet_address: str | None = None

class UserBase(BaseModel):
    wallet_address: str = Field(..., min_length=32, max_length=44)
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    bio: Optional[str] = Field(None, max_length=500)

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    created_at: datetime
    class Config:
        from_attributes = True

class TokenBase(BaseModel):
    contract_address: str
    name: str
    symbol: str
    description: Optional[str] = None
    website: Optional[str] = None
    twitter: Optional[str] = None
    telegram: Optional[str] = None
    discord: Optional[str] = None

class TokenCreate(TokenBase):
    pass

class TokenUpdate(BaseModel):
    name: Optional[str] = None
    symbol: Optional[str] = None
    description: Optional[str] = None
    website: Optional[str] = None
    twitter: Optional[str] = None
    telegram: Optional[str] = None
    discord: Optional[str] = None

class Token(TokenBase):
    id: int
    created_at: datetime
    price: Optional[float] = None
    price_change_24h: Optional[float] = None
    liquidity: Optional[float] = None
    class Config:
        from_attributes = True

class PostBase(BaseModel):
    content: str = Field(..., min_length=1, max_length=280)

class PostCreate(PostBase):
    token_address: Optional[str] = None

class Post(PostBase):
    id: int
    author_wallet: str
    created_at: datetime
    class Config:
        from_attributes = True