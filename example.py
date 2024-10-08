from time import sleep

from core.manager import Manager
from core.managers.cromwell_manager import CromwellManager
from core.visualizer import visualize_gc_content
from core.workflow_validator import validate_wdl
from utils import make_absolute_path

if __name__ == "__main__":
    # prepare files
    wdl_file = "wdls/covid_analysis.wdl"
    output_directory = make_absolute_path("outputs")

    # input options
    input_options = {
        "CoronavirusAnalysis.fasta_file": "data/coronavirus.fasta",
        "CoronavirusAnalysis.gc_content_script": "logics/gc_content.py",
        "CoronavirusAnalysis.sequence_length_script": "logics/sequence_length.py",
        "CoronavirusAnalysis.transcription_script": "logics/transcription.py",
        "CoronavirusAnalysis.pipfile": "logics/Pipfile",
        "CoronavirusAnalysis.pipfile_lock": "logics/Pipfile.lock",
    }
    options = {
        "final_workflow_outputs_dir": output_directory,
        "use_relative_output_paths": True,
    }

    # validate wdl
    validate_wdl(wdl_file)
    if not validate_wdl(wdl_file):
        print("WDL is not valid")
        exit(1)

    # initiate manager
    manager = Manager(CromwellManager())
    manager.authenticate()

    # submit workflow
    submit_result = manager.submit_workflow(wdl_file, input_options, options)
    print(submit_result)

    # wait for workflow to finish
    result = manager.get_workflow_status(submit_result["id"])
    while not result or result[0]["status"] not in ["Succeeded", "Failed"]:
        result = manager.get_workflow_status(submit_result["id"])
        print(result)
        sleep(5)
