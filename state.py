import enum


class WorkingModes(enum.Enum):
    basic = 0
    filesystem = 1


class State:
    working_mode = WorkingModes.basic
    working_dir = None
