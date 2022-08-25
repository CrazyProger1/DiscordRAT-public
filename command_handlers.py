import os
import subprocess
import psutil
from config import Config
from state import State, WorkingModes
from text import *
from exceptions import *
from helpers import *


def help_hndl(config: Config, state: State) -> str:
    return HELP if state.working_mode == WorkingModes.basic else FILESYSTEM_HELP


def exec_hndl(cmd: str, **kwargs) -> str:
    res = os.system(cmd)
    return EXECUTED.format(status=res)


def start_hndl(app: str, **kwargs) -> str:
    os.startfile(app)
    return APPLICATION_STARTED


def chmd_hndl(config: Config, state: State, mode: str) -> str:
    state.working_mode = WorkingModes(int(mode))
    return MODE_CHANGED


def exit_hndl(**kwargs):
    exit(0)


def execo_hndl(config: Config, state: State, cmd: str) -> str:
    result = subprocess.run(
        'chcp 437 && ' + cmd,
        stdout=subprocess.PIPE,
        shell=True
    )
    return result.stdout.decode('utf-8')


def ls_hndl(*args, config: Config, state: State) -> str:
    folder = args[0] if len(args) > 0 else None

    if not folder:
        path = state.working_dir
    else:
        path = folder

    if not os.path.exists(path):
        path = os.path.join(state.working_dir, folder)

    return f'{path} \n\n' + '\n'.join(os.listdir(path))


def dir_hndl(*args, config: Config, state: State) -> str:
    return ls_hndl(
        *args,
        config=config,
        state=state,
    )


def rmde_hndl(config: Config, state: State) -> str:
    state.working_mode = WorkingModes.basic
    return MODE_CHANGED


def shutdown_hndl(time: str = None, **kwargs):
    if time and time.isdigit():
        os.system(f'shutdown /s /f /t {time}')

    os.system(f'shutdown /p')


def kill_hndl(pid: str = None, name: str = None, **kwargs):
    proc = get_proc(name=name, pid=pid)
    if proc:
        proc.kill()
        return KILLED
    else:
        raise CommandExecutionError(PROC_NOT_FOUND)


def prlst_hndl(**kwargs):
    out = '|  name  |  pid  |\n'
    for proc in psutil.process_iter():
        out += f'{proc.name()} <{proc.pid}>\n'

    return out


def susp_hndl(name: str = None, pid: str = None, **kwargs):
    proc = get_proc(name=name, pid=pid)
    if proc:
        proc.suspend()
        return SUSPENDED
    else:
        raise CommandExecutionError(PROC_NOT_FOUND)
