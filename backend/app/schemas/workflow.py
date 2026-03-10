from pydantic import BaseModel
from datetime import datetime


class WorkflowCreate(BaseModel):
    name: str
    description: str | None = None
    definition_json: str


class WorkflowResponse(BaseModel):
    id: int
    name: str
    description: str | None
    definition_json: str
    created_at: datetime

    class Config:
        from_attributes = True