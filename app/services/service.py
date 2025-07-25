import httpx
from typing import Any, Dict

class HttpService:
    def __init__(self):
        self.client = httpx.AsyncClient()

    async def fetch_data(self, url: str, params: Dict[str, Any]):
        response = await self.client.get(url, params=params)
        response.raise_for_status()   # Raises an error if the request was unsuccessful
        return response.json()
    
    async def close(self):
        await self.client.aclose()
