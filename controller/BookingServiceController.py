from fastapi import APIRouter, Request, Response, Depends
from util import check_jwt, RequestHandler
from typing import Annotated
import os


router = APIRouter(prefix="/booking", tags=["Booking Service Gateway"])
request_handler = RequestHandler(
    service_name="Booking",
    service_url=os.getenv("BOOKING_SERVICE_URL")
)

@router.get("/{path}", dependencies=[Depends(check_jwt)])
async def get_booking(path: str, request: Request, response: Response, type: str):
    resp = request_handler.get(
        path=f"/api/v1/booking/{path}?type={type}",
        headers={"Authorization": request.headers.get("Authorization")}
    )
    response.status_code = resp.status_code
    return resp.json()

@router.post("/", dependencies=[Depends(check_jwt)])
async def post_booking(request: Request, response: Response, user:Annotated[dict, Depends(check_jwt)]):
    print(user)
    data = await request.json()
    data["user_id"] = user.get("id")
    resp = request_handler.post(
        path=f"/api/v1/booking/",
        headers={"Authorization": request.headers.get("Authorization")},
        data=data
    )
    response.status_code = resp.status_code
    return resp.json()