import os

from cromwell_tools import api
from cromwell_tools.cromwell_auth import CromwellAuth
from dotenv import load_dotenv
from utils import convert_paths

# .env 파일에서 환경 변수 로드
load_dotenv()

class CromwellManager:
    def __init__(self, cromwell_url=None, auth_options=None):
        self.cromwell_url = cromwell_url or os.getenv("CROMWELL_URL", "http://localhost:8899")
        self.auth_options = auth_options or {}
        self.auth = None

    def authenticate(self):
        if self.auth is not None:
            return self.auth

        self.auth = CromwellAuth.from_no_authentication(
            url=self.cromwell_url,
        )

    def submit_workflow(self, wdl_file, inputs_files=None, dependencies=None):
        # wdl_file, inputs_files, dependencies 경로를 절대 경로로 변환
        wdl_file = convert_paths(wdl_file)
        if inputs_files:
            inputs_files = convert_paths(inputs_files)
        if dependencies:
            dependencies = convert_paths(dependencies)

        result = api.submit(
            auth=self.auth,
            wdl_file=wdl_file,
            inputs_files=inputs_files,
            dependencies=dependencies,
        )
        if result.status_code != 201:
            raise Exception(f"Failed to submit workflow: {result.text}")

        return result.json()

    def get_workflow_status(self, workflow_id):
        result = api.query(
            auth=self.auth,
            query_dict={
                "id": workflow_id,
            }
        )

        if result.status_code != 200:
            raise Exception(f"Failed to get workflow status: {result.text}")

        results = result.json()

        if not results.get("results"):
            raise Exception(f"Workflow not found: {workflow_id}")

        return results["results"][0]

    def abort_workflow(self, workflow_id):
        result = api.abort(
            auth=self.auth,
            uuid=workflow_id,
        )

        if result.status_code != 200:
            raise Exception(f"Failed to abort workflow: {result.text}")

        return result.json()


if __name__ == "__main__":
    wdl_file = "wdls/covid_test_injected.wdl"
    input_files = "wdls/inputs_covid_test.json"
    cromwell_manager = CromwellManager()
    cromwell_manager.authenticate()
    result = cromwell_manager.submit_workflow(wdl_file, input_files)
    print(result)
