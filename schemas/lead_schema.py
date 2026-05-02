from pydantic import BaseModel

class LeadCreate(BaseModel):
    full_name: str
    phone: str
    email: str
    preferred_location: str
    budget: str
    source: str
    assigned_agent: str
    notes: str