"""Many useful funcs"""

import psutil
import os
from text import *
from exceptions import *


def get_proc(name: str = None, pid: str = None) -> psutil.Process:
    for proc in psutil.process_iter():
        if name and proc.name() == name:
            return proc
        elif pid and pid.isdigit() and pid == proc.pid:
            return proc


def remove_quotes(element: str):
    element = element.strip()
    if element[0] == "'":
        return element[1:-1]
    else:
        return element


def check_existence(src: str, dest: str):
    if not os.path.exists(src):
        raise CommandExecutionError(SRC_NOT_EXISTS)
    if not os.path.exists(dest):
        raise CommandExecutionError(DEST_NOT_EXISTS)
