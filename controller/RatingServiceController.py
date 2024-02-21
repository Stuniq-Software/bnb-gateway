from fastapi import APIRouter, Request, Response, Depends
from util import check_jwt, RequestHandler
from typing import Annotated
import os


router = APIRouter(prefix="/rating", tags=["Rating Service Gateway"])
request_handler = RequestHandler(
    service_name="Rating",
    service_url=os.getenv("RATING_SERVICE_URL")
)

@router.get("/{path}", dependencies=[Depends(check_jwt)])
async def get_booking(path: str, request: Request, response: Response, id_type: str):
    resp = request_handler.get(
        path=f"/api/v1/ratings/{path}?id_type={id_type}",
        headers={"Authorization": request.headers.get("Authorization")}
    )
    response.status_code = resp.status_code
    return resp.json()

@router.post("/", dependencies=[Depends(check_jwt)])
async def post_booking(request: Request, response: Response, user: Annotated[dict, Depends(check_jwt)]):
    data = await request.json()
    data["user_id"] = user.get("id")
    resp = request_handler.post(
        path=f"/api/v1/ratings/",
        headers={"Authorization": request.headers.get("Authorization")},
        data=data
    )
    response.status_code = resp.status_code
    return resp.json()

@router.put("/{path}", dependencies=[Depends(check_jwt)])
async def put_booking(path: str, request: Request, response: Response):
    resp = request_handler.put(
        path=f"/api/v1/ratings/{path}",
        headers={"Authorization": request.headers.get("Authorization")},
        data=await request.json()
    )
    response.status_code = resp.status_code
    return resp.json()