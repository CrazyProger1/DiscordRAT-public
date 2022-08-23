import os

from config import Config
from state import State
from text import *


def help_hndl(config: Config, state: State) -> str:
    return HELP


def exec_hndl(config: Config, state: State, cmd: str) -> str:
    os.system(cmd)
    return EXECUTED
