from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.db import engine, Base
from models.lead import Lead
from routes.lead_routes import router as lead_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(lead_router)

@app.get("/")
def home():
    return {"message": "Gharpayy CRM Backend Running Successfully"}