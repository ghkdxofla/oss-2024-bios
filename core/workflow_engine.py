import subprocess


def run_workflow(request):
    wdl_script = "wdls/covid_analysis.wdl"
    inputs_json = {
        "Covid19Analysis.fastq1": request.fastq1,
        "Covid19Analysis.fastq2": request.fastq2,
        "Covid19Analysis.reference_fasta": request.reference_fasta,
        "Covid19Analysis.sample_name": request.sample_name
    }

    with open("inputs.json", "w") as f:
        json.dump(inputs_json, f)

    result = subprocess.run(["java", "-jar", "cromwell.jar", "run", wdl_script, "-i", "inputs.json"],
                            capture_output=True, text=True)

    if result.returncode != 0:
        raise RuntimeError(f"Workflow execution failed: {result.stderr}")

    return {"stdout": result.stdout, "stderr": result.stderr}
