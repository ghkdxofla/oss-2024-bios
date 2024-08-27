from core.managers.cromwell_manager import CromwellManager


class Manager:
    def __init__(self, manager: CromwellManager):
        self._manager = manager

    def authenticate(self):
        return self._manager.authenticate()

    def submit_workflow(self, wdl_file, inputs_files=None, option_file=None, dependencies=None):
        # FIXME: wdl_file, inputs_files, dependencies 추상화
        return self._manager.submit_workflow(wdl_file, inputs_files, option_file, dependencies)

    def get_workflow_status(self, workflow_id):
        return self._manager.get_workflow_status(workflow_id)

    def abort_workflow(self, workflow_id):
        return self._manager.abort_workflow(workflow_id)
