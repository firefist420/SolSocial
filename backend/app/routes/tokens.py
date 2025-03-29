from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import TokenCreate, TokenUpdate, Token
from ..crud import get_token_by_contract, create_token, get_token, update_token
from ..auth import get_current_user
from .. import models

router = APIRouter(prefix="/tokens", tags=["tokens"])

@router.post("/", response_model=Token)
def create_token(
    token: TokenCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    db_token = get_token_by_contract(db, token.contract_address)
    if db_token:
        raise HTTPException(status_code=400, detail="Token already exists")
    return create_token(db, token, current_user.wallet_address)

@router.get("/{contract_address}", response_model=Token)
def read_token(contract_address: str, db: Session = Depends(get_db)):
    db_token = get_token_by_contract(db, contract_address)
    if db_token is None:
        raise HTTPException(status_code=404, detail="Token not found")
    return db_token

@router.put("/{token_id}", response_model=Token)
def update_token(
    token_id: int,
    token: TokenUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    db_token = get_token(db, token_id)
    if not db_token:
        raise HTTPException(status_code=404, detail="Token not found")
    if db_token.creator_wallet != current_user.wallet_address:
        raise HTTPException(status_code=403, detail="Not authorized to update this token")
    return update_token(db, token_id=token_id, token_update=token)