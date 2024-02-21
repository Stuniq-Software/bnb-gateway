from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from controller import (AuthServiceController, 
                        StayServiceController, 
                        BookingServiceController, 
                        PaymentServiceController, 
                        InvoiceServiceController, 
                        RatingServiceController)
from util import health_check


app = FastAPI(
    title="BnB Clone API Gateway",
    description="A simple API Gateway for BnB Clone",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    contact={
        "name": "Abhiram B.S.N.",
        "email": "abhirambsn@gmail.com",
        "url": "https://abhirambsn.com"
    }
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def perform_health_check(response: Response):
    return health_check()

@app.get("/healthz")
async def perform_healthz_check(response: Response):
    return health_check()

app.include_router(AuthServiceController)
app.include_router(StayServiceController)
app.include_router(BookingServiceController)
app.include_router(PaymentServiceController)
app.include_router(InvoiceServiceController)
app.include_router(RatingServiceController)