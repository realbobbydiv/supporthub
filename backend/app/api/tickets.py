from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.session import get_db
from app.db.crud_tickets import create_ticket, list_tickets, get_ticket, update_ticket
from app.schemas.tickets import TicketCreate, TicketOut, TicketUpdate
from app.models.user import User
from app.schemas.tickets import TicketStats
from app.db.crud_tickets import get_ticket_stats


router = APIRouter(prefix="/tickets", tags=["tickets"])


@router.post("", response_model=TicketOut, status_code=201)
def create(payload: TicketCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return create_ticket(db, payload.title, payload.description, payload.priority, user.id)


@router.get("", response_model=list[TicketOut])
def list_all(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return list_tickets(db)

@router.get("/stats", response_model=TicketStats)
def stats(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return get_ticket_stats(db)
 
@router.get("/{ticket_id}", response_model=TicketOut)
def get_one(ticket_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    t = get_ticket(db, ticket_id)
    if not t:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return t


@router.patch("/{ticket_id}", response_model=TicketOut)
def update(
    ticket_id: int,
    payload: TicketUpdate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    t = get_ticket(db, ticket_id)
    if not t:
        raise HTTPException(status_code=404, detail="Ticket not found")

    return update_ticket(db, t, payload.dict(exclude_unset=True))
