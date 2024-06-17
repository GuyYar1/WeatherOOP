# debug_utils.py
import os


def debug_print(text):
    # pYCHARM ENV VVARIABLE DOESNT  WORK." SET IT ON SUSER ENV VAR AND JUST CHANGE IT
    debug_mode = False  # os.getenv('DEBUG_MODE') == 'true'
    if debug_mode:
        print(text)
