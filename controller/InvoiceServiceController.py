from fastapi import APIRouter, Request, Response, Depends
from util import check_jwt, RequestHandler
import os


router = APIRouter(prefix="/invoice", tags=["Invoice Service Gateway"])
request_handler = RequestHandler(
    service_name="Invoice",
    service_url=os.getenv("INVOICE_SERVICE_URL")
)

@router.get("/{path}", dependencies=[Depends(check_jwt)])
async def get_invoice(path: str, request: Request, response: Response):
    resp = request_handler.get(
        path=f"/api/v1/invoice/{path}",
        headers={"Authorization": request.headers.get("Authorization")}
    )
    response.status_code = resp.status_code
    return resp.json()
