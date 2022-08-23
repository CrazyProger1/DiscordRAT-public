import enum
import sys
import os


class WorkingModes(enum.Enum):
    basic = 0
    filesystem = 1


class State:
    working_mode = WorkingModes.basic
    working_dir = os.path.split(sys.argv[0])[0]
