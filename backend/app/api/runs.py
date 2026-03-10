from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.workflow_run import WorkflowRun
from app.schemas.workflow_run import WorkflowRunResponse

router = APIRouter()


@router.get("/runs", response_model=list[WorkflowRunResponse])
def list_runs(db: Session = Depends(get_db)):
    runs = db.query(WorkflowRun).order_by(WorkflowRun.id.desc()).all()
    return runs


@router.get("/runs/{run_id}", response_model=WorkflowRunResponse)
def get_run(run_id: int, db: Session = Depends(get_db)):
    run = db.query(WorkflowRun).filter(WorkflowRun.id == run_id).first()

    if not run:
        raise HTTPException(status_code=404, detail="Run not found")

    return run