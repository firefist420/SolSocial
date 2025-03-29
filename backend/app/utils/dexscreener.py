import httpx
from typing import Optional, Dict
import os

DEXSCREENER_API = os.getenv("DEXSCREENER_API", "https://api.dexscreener.com")

async def get_token_data(token_address: str) -> Optional[Dict]:
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{DEXSCREENER_API}/latest/dex/tokens/{token_address}")
            response.raise_for_status()
            data = response.json()
            return data.get("pairs", [{}])[0] if data.get("pairs") else None
    except Exception as e:
        print(f"Error fetching token data: {e}")
        return None