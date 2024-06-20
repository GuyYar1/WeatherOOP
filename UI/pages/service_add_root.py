import os
import sys

class Serviceaddroot:

    @staticmethod
    def support_abs_sys_path():

        # Get the absolute path of the project root
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        # Add the project root to Python's search path
        if project_root not in sys.path:
            sys.path.insert(0, project_root)


