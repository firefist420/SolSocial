from solders.pubkey import Pubkey
from solders.message import Message

def verify_solana_token(address: str) -> bool:
    try:
        Pubkey.from_string(address)
        return True
    except ValueError:
        return False

def verify_wallet_signature(wallet_address: str, signed_message: list, message: str) -> bool:
    try:
        pubkey = Pubkey.from_string(wallet_address)
        msg = Message.new(bytes(message, 'utf-8'))
        return pubkey.verify(msg, bytes(signed_message))
    except Exception:
        return False