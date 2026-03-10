from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.db import Base


class WorkflowRun(Base):
    __tablename__ = "workflow_runs"

    id = Column(Integer, primary_key=True, index=True)

    workflow_id = Column(Integer, ForeignKey("workflows.id"), nullable=False)

    status = Column(String(50), nullable=False, default="pending")

    input_text = Column(Text, nullable=False)

    output_json = Column(Text, nullable=True)

    error_message = Column(Text, nullable=True)

    started_at = Column(DateTime(timezone=True), server_default=func.now())

    finished_at = Column(DateTime(timezone=True), nullable=True)