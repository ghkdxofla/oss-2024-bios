import unittest

from api.models import WorkflowRequest
from core.workflow_engine import run_workflow


class TestCovid19Workflow(unittest.TestCase):
    def test_workflow_execution(self):
        request = WorkflowRequest(
            fastq1="sample_R1.fastq",
            fastq2="sample_R2.fastq",
            reference_fasta="reference.fasta",
            sample_name="covid_sample",
        )

        result = run_workflow(request)
        self.assertIn("stdout", result)
        self.assertIn("stderr", result)


if __name__ == "__main__":
    unittest.main()
