import os

import requests
from dotenv import load_dotenv
from utils import convert_paths

# .env 파일에서 환경 변수 로드
load_dotenv()


def validate_wdl(wdl_file, cromwell_url=None):
    base_url = cromwell_url or os.getenv("CROMWELL_URL", "http://localhost:8899")
    url = f"{base_url}/api/womtool/v1/describe"

    wdl_file = convert_paths(wdl_file)
    with open(wdl_file, 'rb') as file_data:
        files = {'workflowSource': file_data}
        response = requests.post(url, files=files)

    result = response.json()
    if response.status_code == 200:
        return result.get('validWorkflow'), result.get('errors')
    else:
        return False, response.text
