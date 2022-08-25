import psutil


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
