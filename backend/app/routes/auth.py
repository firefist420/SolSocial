from fastapi import APIRouter, Depends, HTTPException, status, Form
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import Token, WalletAuthRequest, UserCreate
from ..crud import get_user, create_user
from ..auth import create_access_token, verify_wallet_signature

router = APIRouter(tags=["auth"])

@router.post("/token", response_model=Token)
async def login_for_access_token(
    wallet_auth: WalletAuthRequest,
    db: Session = Depends(get_db)
):
    if not verify_wallet_signature(wallet_auth.wallet_address, wallet_auth.signed_message, wallet_auth.message):
        raise HTTPException(status_code=400, detail="Invalid signature")
    
    user = get_user(db, wallet_auth.wallet_address)
    if not user:
        user = create_user(db, UserCreate(wallet_address=wallet_auth.wallet_address))
    
    access_token = create_access_token(data={"sub": user.wallet_address})
    return {"access_token": access_token, "token_type": "bearer"}