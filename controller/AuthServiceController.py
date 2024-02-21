from fastapi import APIRouter, Request, Response, Depends
from util import check_jwt, RequestHandler
import os


router = APIRouter(prefix="/auth", tags=["Authentication Gateway"])
request_handler = RequestHandler(
    service_name="Authentication",
    service_url=os.getenv("AUTH_SERVICE_URL")
)

@router.get("/token")
async def login(request: Request, response: Response):
    resp = request_handler.get(
        path="/api/v1/auth/token",
        headers={"Authorization": request.headers.get("Authorization")}
    )
    response.status_code = resp.status_code
    return resp.json()

@router.post("/")
async def create_user(request: Request, response: Response):
    resp = request_handler.post(
        path="/api/v1/auth/",
        data=await request.json()
    )
    response.status_code = resp.status_code
    return resp.json()

@router.get("/{path}", dependencies=[Depends(check_jwt)])
async def auth(request: Request, response: Response, path: str, user=Depends(check_jwt)):
    ms_path = f"/api/v1/auth/{path}"
    resp = request_handler.get(
        path=ms_path,
        headers={"Authorization": request.headers.get('Authorization')}
    )
    response.status_code = resp.status_code
    return resp.json()

@router.post("/{path}", dependencies=[Depends(check_jwt)])
async def auth(request: Request, response: Response, path: str):
    ms_path = f"/api/v1/auth/{path}"
    resp = request_handler.post(
        path=ms_path,
        headers={"Authorization": request.headers.get('Authorization')},
        data=await request.json()
    )
    response.status_code = resp.status_code
    return resp.json()