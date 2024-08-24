import os


def make_absolute_path(path):
    """
    주어진 경로가 절대 경로가 아니라면, 현재 파일의 상위 디렉토리를 기준으로 절대 경로를 반환합니다.
    """
    if path.startswith("/"):
        return path
    else:
        root_dir = os.path.abspath(os.path.dirname(__file__))
        return os.path.join(root_dir, path)


def convert_paths(paths):
    """
    경로 리스트의 각 항목을 절대 경로로 변환합니다.
    """
    if isinstance(paths, list):
        return [make_absolute_path(path) for path in paths]
    elif isinstance(paths, str):
        return make_absolute_path(paths)
    return paths
