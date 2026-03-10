from pydantic import BaseModel
from datetime import datetime


class WorkflowRunCreate(BaseModel):
    input_text: str


class WorkflowRunResponse(BaseModel):
    id: int
    workflow_id: int
    status: str
    input_text: str
    output_json: str | None
    error_message: str | None
    started_at: datetime
    finished_at: datetime | None

    class Config:
        from_attributes = True