from sqlalchemy.orm import Session
from app.models.ticket import Ticket


def create_ticket(db: Session, title: str, description: str | None, priority: str, created_by_id: int) -> Ticket:
    t = Ticket(
        title=title,
        description=description,
        priority=priority,
        created_by_id=created_by_id,
    )
    db.add(t)
    db.commit()
    db.refresh(t)
    return t


def list_tickets(db: Session) -> list[Ticket]:
    return db.query(Ticket).order_by(Ticket.id.desc()).all()


def get_ticket(db: Session, ticket_id: int) -> Ticket | None:
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()


def update_ticket(db: Session, ticket: Ticket, data: dict) -> Ticket:
    for key, value in data.items():
        setattr(ticket, key, value)
    db.commit()
    db.refresh(ticket)
    return ticket
from sqlalchemy import func
from app.models.ticket import Ticket


def get_ticket_stats(db):
    total = db.query(func.count(Ticket.id)).scalar() or 0

    by_status_rows = (
        db.query(Ticket.status, func.count(Ticket.id))
        .group_by(Ticket.status)
        .all()
    )

    by_priority_rows = (
        db.query(Ticket.priority, func.count(Ticket.id))
        .group_by(Ticket.priority)
        .all()
    )

    by_status = {status: count for status, count in by_status_rows if status}
    by_priority = {priority: count for priority, count in by_priority_rows if priority}

    return {
        "total": total,
        "by_status": by_status,
        "by_priority": by_priority,
    }
