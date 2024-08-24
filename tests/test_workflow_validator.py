from core.workflow_validator import validate_wdl


def test_validate_workflow__when__using_valid_wdl__expect__true():
    wdl_file = "tests/data/valid_workflow.wdl"

    success, message = validate_wdl(wdl_file)
    assert success is True


def test_validate_workflow__when__using_invalid_wdl__expect__false():
    wdl_file = "tests/data/invalid_workflow.wdl"

    success, message = validate_wdl(wdl_file)
    assert success is False

