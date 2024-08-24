# cromwell_runner/validator.py
import subprocess

def validate_wdl(wdl_file, cromwell_jar="cromwell.jar"):
    """
    Validates a WDL file using Cromwell's validate command.

    :param wdl_file: Path to the WDL file to validate.
    :param cromwell_jar: Path to the Cromwell JAR file.
    :return: True if the WDL file is valid, False otherwise.
    """
    try:
        result = subprocess.run(
            ["java", "-jar", cromwell_jar, "validate", wdl_file],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode == 0:
            print(f"Validation successful for {wdl_file}")
            return True
        else:
            print(f"Validation failed for {wdl_file}")
            print(result.stdout)
            print(result.stderr)
            return False

    except Exception as e:
        print(f"An error occurred during validation: {str(e)}")
        return False
