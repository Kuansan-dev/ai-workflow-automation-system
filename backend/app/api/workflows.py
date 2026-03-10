from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.workers.tasks import execute_workflow_task
from app.models.workflow import Workflow
from app.schemas.workflow import WorkflowCreate, WorkflowResponse
from app.core.database import get_db

from fastapi import HTTPException
from app.models.workflow_run import WorkflowRun
from app.schemas.workflow_run import WorkflowRunCreate, WorkflowRunResponse
from app.services.workflow_executor import execute_workflow
from datetime import datetime

router = APIRouter()


@router.post("/workflows", response_model=WorkflowResponse)
def create_workflow(workflow: WorkflowCreate, db: Session = Depends(get_db)):

    new_workflow = Workflow(
        name=workflow.name,
        description=workflow.description,
        definition_json=workflow.definition_json,
    )

    db.add(new_workflow)
    db.commit()
    db.refresh(new_workflow)

    return new_workflow


@router.get("/workflows", response_model=list[WorkflowResponse])
def list_workflows(db: Session = Depends(get_db)):

    workflows = db.query(Workflow).all()

    return workflows

@router.post("/workflows/{workflow_id}/run", response_model=WorkflowRunResponse)
def run_workflow(workflow_id: int, payload: WorkflowRunCreate, db: Session = Depends(get_db)):

    workflow = db.query(Workflow).filter(Workflow.id == workflow_id).first()

    if not workflow:
        raise HTTPException(status_code=404, detail="Workflow not found")

    run = WorkflowRun(
        workflow_id=workflow.id,
        status="pending",
        input_text=payload.input_text,
    )

    db.add(run)
    db.commit()
    db.refresh(run)

    execute_workflow_task.delay(run.id)

    return run