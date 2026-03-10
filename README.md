# AI Workflow Automation System

An asynchronous AI workflow orchestration platform built with FastAPI, Celery, Redis, and PostgreSQL.

This system allows users to define workflows consisting of AI-powered steps (such as summarization or task extraction) and execute them asynchronously using distributed workers.

---

## Architecture

Client → FastAPI API → Redis Queue → Celery Worker → AI Execution → PostgreSQL

The system uses a message queue to distribute workflow execution tasks to background workers.

---

## Features

• Create AI workflows  
• Execute workflows asynchronously  
• Extract tasks from meeting notes using LLMs  
• Store workflow results and execution history  
• Background processing with Celery workers  
• REST API with interactive Swagger documentation  
• Docker-based infrastructure  

---

## Tech Stack

Backend
- Python
- FastAPI
- SQLAlchemy

Infrastructure
- Docker
- Redis
- PostgreSQL
- Celery

AI Integration
- OpenAI API

---

## Project Structure


backend/
app/
api/ → API routes
services/ → AI and workflow logic
workers/ → Celery tasks
models/ → database models
schemas/ → API schemas
core/ → configuration

infra/
docker-compose.yml


---

## Setup Instructions

### 1 Install dependencies


cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt


---

### 2 Start infrastructure


cd infra
docker compose up -d


This starts:

- PostgreSQL
- Redis

---

### 3 Run FastAPI


cd backend
uvicorn app.main:app --reload


Swagger API documentation:


http://127.0.0.1:8000/docs


---

### 4 Start Celery worker


celery -A app.workers.celery_app.celery_app worker --loglevel=info --pool=solo


---

## Example Workflow

Example workflow definition:


{
"name": "Document Processor",
"description": "Summarize and extract tasks",
"definition_json": {
"steps": ["summarize", "tasks"]
}
}


Run the workflow with:


POST /workflows/{workflow_id}/run


Example input:


{
"input_text": "Meeting notes: John must finish the report tomorrow."
}


Result:


{
"status": "completed",
"output_json": "Tasks extracted from meeting notes..."
}


---

## Future Improvements

• Visual workflow builder  
• Workflow scheduling  
• Multi-step agent workflows  
• Kubernetes deployment  
• Streaming AI responses  

---

## Author

Sanzhar Kuanysh  
BSc Artificial Intelligence — Vrije Universiteit Amsterdam