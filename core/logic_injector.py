import importlib
import os
from types import ModuleType
from dotenv import load_dotenv
from utils import convert_paths

# .env 파일에서 환경 변수 로드
load_dotenv()

def inject_logic(wdl_file, logic_module: str | ModuleType, output_file=None) -> tuple[bool, str]:
    # 모듈 import
    try:
        if isinstance(logic_module, str):
            module = importlib.import_module(logic_module)
        else:
            module = logic_module
    except ImportError:
        return False, f"Error: Could not import module {logic_module}"

    # 모듈의 절대 경로 출력
    module_path = os.path.abspath(module.__file__)
    wdl_file = convert_paths(wdl_file)

    # WDL 파일 읽기
    with open(wdl_file, 'r') as wdl:
        wdl_content = wdl.read()

    # 내용 주입
    module_name = module.__name__.split('.')[-1]
    injected_content = wdl_content.replace(f"<<{module_name}>>", module_path)

    if output_file is None:
        output_file = wdl_file
    else:
        output_file = convert_paths(output_file)

    # 수정된 WDL 파일 쓰기
    with open(output_file, 'w') as output_wdl:
        output_wdl.write(injected_content)

    return True, f"Success: Injected logic from {logic_module} into {wdl_file}"


if __name__ == "__main__":
    wdl_file = "wdls/covid_test.wdl"
    import logics.gc_content as gc_content
    import logics.sequence_length as sequence_length

    inject_logic(wdl_file, gc_content, "wdls/covid_test_injected.wdl")
    inject_logic("wdls/covid_test_injected.wdl", sequence_length, "wdls/covid_test_injected.wdl")


