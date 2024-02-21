from fastapi import APIRouter, Request, Response, Depends
from util import check_jwt, RequestHandler
import os


router = APIRouter(prefix="/auth", tags=["Stay Service Gateway"])
request_handler = RequestHandler(
    service_name="Stay",
    service_url=os.getenv("STAY_SERVICE_URL")
)

@router.get("/{path}", dependencies=[Depends(check_jwt)])
async def get_stay(request: Request, response: Response):
    resp = request_handler.get(
        path="/api/v1/stays/{path}",
        headers={"Authorization": request.headers.get("Authorization")}
    )
    response.status_code = resp.status_code
    return resp.json()

@router.post("/{path}", dependencies=[Depends(check_jwt)])
async def post_stay(path: str, request: Request, response: Response):
    resp = request_handler.post(
        path=f"/api/v1/stays/{path}",
        headers={"Authorization": request.headers.get("Authorization")},
        data=await request.json()
    )
    response.status_code = resp.status_code
    return resp.json()