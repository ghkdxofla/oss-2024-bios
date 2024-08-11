from pydantic import BaseModel

class WorkflowRequest(BaseModel):
    fastq1: str
    fastq2: str
    reference_fasta: str
    sample_name: str

class WorkflowResponse(BaseModel):
    result: dict
