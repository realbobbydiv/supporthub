from pydantic import BaseModel
from typing import Dict


class TicketCreate(BaseModel):
    title: str
    description: str | None = None
    priority: str = "medium"


class TicketUpdate(BaseModel):
    status: str | None = None
    priority: str | None = None
    assigned_to_id: int | None = None


class TicketOut(BaseModel):
    id: int
    title: str
    description: str | None
    status: str
    priority: str
    created_by_id: int
    assigned_to_id: int | None

    class Config:
        from_attributes = True


class TicketStats(BaseModel):
    total: int
    by_status: Dict[str, int]
    by_priority: Dict[str, int]
