from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
import models, schemas
from database import engine, SessionLocal
from analyzer import analyze_ticket

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/tickets/analyze", response_model=schemas.TicketResponse)
def analyze(ticket: schemas.TicketCreate, db: Session = Depends(get_db)):
    category, priority, confidence = analyze_ticket(ticket.message)

    db_ticket = models.Ticket(
        message=ticket.message,
        category=category,
        priority=priority,
        confidence=confidence
    )

    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)

    return db_ticket

@app.get("/tickets", response_model=list[schemas.TicketResponse])
def get_tickets(db: Session = Depends(get_db)):
    return db.query(models.Ticket).order_by(models.Ticket.id.desc()).all()