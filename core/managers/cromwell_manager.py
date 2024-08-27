import json
import os
from io import BytesIO

from cromwell_tools import api
from cromwell_tools.cromwell_auth import CromwellAuth
from dotenv import load_dotenv
from utils import convert_paths

# .env 파일에서 환경 변수 로드
load_dotenv()

class CromwellManager:
    def __init__(self, cromwell_url=None, auth_options=None):
        self.url = cromwell_url or os.getenv("CROMWELL_URL", "http://localhost:8899")
        self.auth_options = auth_options or {}
        self.auth = None

    def authenticate(self):
        if self.auth is not None:
            return self.auth

        self.auth = CromwellAuth.from_no_authentication(
            url=self.url,
        )

    def submit_workflow(self, wdl_file, inputs_files=None, options_file=None, dependencies=None):
        # TODO: wdl_file, inputs_files, options_file, dependencies 경로를 절대 경로로 변환
        # TODO: list[dict]나 dict에 대한 변환 처리 일괄 적용
        wdl_file = convert_paths(wdl_file)
        if inputs_files:
            if isinstance(inputs_files, dict):
                input_options_json = json.dumps(inputs_files)
                inputs_files = BytesIO(input_options_json.encode('utf-8'))
            else:
                inputs_files = convert_paths(inputs_files)
        if dependencies:
            dependencies = convert_paths(dependencies)
        if options_file:
            if isinstance(options_file, dict):
                options_json = json.dumps(options_file)
                options_file = BytesIO(options_json.encode('utf-8'))
            else:
                options_file = convert_paths(options_file)


        result = api.submit(
            auth=self.auth,
            wdl_file=wdl_file,
            inputs_files=inputs_files,
            options_file=options_file,
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

        return results["results"]

    def abort_workflow(self, workflow_id):
        result = api.abort(
            auth=self.auth,
            uuid=workflow_id,
        )

        if result.status_code != 200:
            raise Exception(f"Failed to abort workflow: {result.text}")

        return result.json()
