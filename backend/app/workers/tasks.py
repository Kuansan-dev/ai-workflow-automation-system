from datetime import datetime

from app.db import SessionLocal
from app.models.workflow import Workflow
from app.models.workflow_run import WorkflowRun
from app.services.workflow_executor import execute_workflow
from app.workers.celery_app import celery_app


@celery_app.task
def execute_workflow_task(run_id: int):
    db = SessionLocal()

    try:
        run = db.query(WorkflowRun).filter(WorkflowRun.id == run_id).first()

        if not run:
            return

        workflow = db.query(Workflow).filter(Workflow.id == run.workflow_id).first()

        if not workflow:
            run.status = "failed"
            run.error_message = "Workflow not found"
            db.commit()
            return

        run.status = "running"
        db.commit()

        output = execute_workflow(workflow.definition_json, run.input_text)

        run.status = "completed"
        run.output_json = output
        run.finished_at = datetime.utcnow()
        db.commit()

    except Exception as e:
        run = db.query(WorkflowRun).filter(WorkflowRun.id == run_id).first()
        if run:
            run.status = "failed"
            run.error_message = str(e)
            db.commit()

    finally:
        db.close()