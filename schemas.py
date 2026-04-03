from pydantic import BaseModel

class TicketCreate(BaseModel):
    message: str

class TicketResponse(BaseModel):
    id: int
    message: str
    category: str
    priority: str
    confidence: float

    class Config:
        from_attributes = True