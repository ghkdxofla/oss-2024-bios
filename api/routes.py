from fastapi import APIRouter, HTTPException
from core.workflow_engine import run_workflow
from api.models import WorkflowRequest, WorkflowResponse

router = APIRouter()

@router.post("/workflow/", response_model=WorkflowResponse)
def submit_workflow(request: WorkflowRequest):
    try:
        result = run_workflow(request)
        return WorkflowResponse(result=result)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
