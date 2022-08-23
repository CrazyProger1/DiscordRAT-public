import os
import subprocess

from config import Config
from state import State, WorkingModes
from text import *


def help_hndl(config: Config, state: State) -> str:
    return HELP


def exec_hndl(config: Config, state: State, cmd: str) -> str:
    os.system(cmd)
    return EXECUTED


def start_hndl(config: Config, state: State, app: str) -> str:
    os.startfile(app)
    return APPLICATION_STARTED


def chmode_hndl(config: Config, state: State, mode: str) -> str:
    if not mode.isdigit():
        raise ValueError('mode must be an integer')

    state.working_mode = WorkingModes(int(mode))
    return 'Mode changed'


def exit_hndl(config: Config, state: State):
    exit(0)


def execo_hndl(config: Config, state: State, cmd: str) -> str:
    result = subprocess.run('chcp 437 && ' + cmd, stdout=subprocess.PIPE, shell=True)
    return result.stdout.decode('utf-8')
