import httpx 
from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Optional, Dict, List, Any

# from ..dependencies import get_token_header
from ..services.service import HttpService
from ..utills.utils import Utills

# router = APIRouter(
#     prefix="/v1",
#     tags=["bikes"],
#     dependencies=[Depends(get_token_header)],
#     responses={404: {"description": "Not found"}},
# )
router = APIRouter(
    prefix="/v1",
    tags=["bikes"])

async def get_http_service():
    service = HttpService()
    try:
        yield service
    finally:
        await service.close()


@router.get("/search")
async def read_item(location: str, duration: int=Query(title="Duration", 
                    description="Duration in Months"), 
                    stolenness: str = 'stolen', 
                    page=1, per_page=25,
                    http_service: HttpService = Depends(get_http_service), 
                    distance: Optional[str] = None,
                    manufacturer: Optional[str] = None) -> List[Dict[str, Any]]:
    """routes to bike search with the params"""
    url = "https://bikeindex.org/api/v3/search"
    params = {
        "location": location,
        "distance": distance,
        "page": page,
        "per_page": per_page,
        "stolenness": stolenness,
        "duration": duration
    }
    if manufacturer:
        params['manufacturer'] = manufacturer
    try:
        data = await http_service.fetch_data(url, params)
        api_data = Utills.get_stolen_bikes_details(data)
        return api_data
    except httpx.HTTPStatusError as exc:
        raise HTTPException(status_code=exc.response.status_code, detail=str(exc))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))