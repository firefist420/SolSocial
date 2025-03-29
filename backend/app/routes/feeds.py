from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..utils.dexscreener import get_token_data

router = APIRouter(prefix="/feeds", tags=["feeds"])

@router.get("/token/{contract_address}")
async def get_token_feed(contract_address: str, db: Session = Depends(get_db)):
    return get_token_data(contract_address)