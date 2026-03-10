from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from app.db import Base


class Workflow(Base):
    __tablename__ = "workflows"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=False)

    description = Column(Text, nullable=True)

    definition_json = Column(Text, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())