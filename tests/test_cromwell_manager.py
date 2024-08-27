from core.managers.cromwell_manager import CromwellManager

def test_submit_workflow():
    manager = CromwellManager()
    manager.authenticate()
    response = manager.submit_workflow("wdls/covid_test.wdl", inputs_files=['wdls/inputs.json'], dependencies=['wdls/covid_test.wdl'])
    assert "id" in response
    assert "status" in response


def test_get_workflow_status():
    manager = CromwellManager()
    manager.authenticate()
    response = manager.get_workflow_status('7a8ea5dd-a8ad-4845-8c9f-80bcca62bbaa')
    assert "status" in response[0]


def test_abort_workflow():
    manager = CromwellManager()
    manager.authenticate()
    response = manager.abort_workflow('7a8ea5dd-a8ad-4845-8c9f-80bcca62bbaa')
    assert "status" in response
