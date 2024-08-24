# cromwell_runner/injector.py
import shutil
import os

def inject_logic(wdl_file, logic_script, output_file):
    """
    Injects custom Python logic into a WDL task.

    :param wdl_file: Path to the WDL file.
    :param logic_script: Path to the Python script to inject.
    :param output_file: Path to the output WDL file with injected logic.
    """
    try:
        with open(wdl_file, 'r') as wdl, open(logic_script, 'r') as logic:
            wdl_content = wdl.read()
            logic_content = logic.read()

        # Insert the Python logic at the appropriate place
        injected_content = wdl_content.replace("python3 <<CODE", f"python3 {logic_script}")

        with open(output_file, 'w') as output_wdl:
            output_wdl.write(injected_content)

        print(f"Logic injected successfully into {output_file}")

    except Exception as e:
        print(f"An error occurred during logic injection: {str(e)}")

