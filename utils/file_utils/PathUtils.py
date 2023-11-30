from pathlib import Path


class PathUtils:

    @staticmethod
    def get_root_project_dir():
        return Path(__file__).absolute().parent.parent.parent
