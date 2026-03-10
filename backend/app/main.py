from fastapi import FastAPI
from app.db import engine, Base

import app.models.workflow
import app.models.workflow_run

from app.api import workflows
from app.api import runs

app = FastAPI(title="AI Workflow Automation System")

Base.metadata.create_all(bind=engine)

app.include_router(workflows.router)
app.include_router(runs.router)

@app.get("/")
def root():
    return {"message": "AI Workflow Automation API is running"}