from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import SessionLocal
from models.lead import Lead
from schemas.lead_schema import LeadCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/leads")
def create_lead(lead: LeadCreate, db: Session = Depends(get_db)):
    new_lead = Lead(**lead.dict())
    db.add(new_lead)
    db.commit()
    db.refresh(new_lead)
    return new_lead

@router.get("/leads")
def get_leads(db: Session = Depends(get_db)):
    return db.query(Lead).all()