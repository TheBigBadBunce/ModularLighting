import builtins as __builtin__

from timeutils import get_current_time
from constants import LOGFILE_REALTIME, LOGFILE_SIMULATE
from arguments import get_args

def add_timestamp(line):
    """Adds timestamp to output"""
    return get_current_time().strftime('%H:%M:%S') + " ~ " + line

def get_logfile_name():
    time_emulation = get_args().mode
    if time_emulation == "realtime":
        return LOGFILE_REALTIME
    elif time_emulation == "simulate":
        return LOGFILE_SIMULATE
    else:
        raise NotImplementedError()

def write_to_logfile(line):
    """Write to log with timestamp"""
    file = open(get_logfile_name(), "a")
    file.write(line)
    file.write('\n')
    file.close()

def reset_logfile():
    """Resets logfile to empty, USE WITH CAUTION! 
       Intended use case: clear logfile before simulated lighting
    """
    file = open(get_logfile_name(), "w")
    file.write("")
    file.close()

def print(line):
    """Print under normal (non-silent) circumstances"""
    line = add_timestamp(str(line))
    if not get_args().silent:
        write_to_logfile(line)
        return __builtin__.print(line)
    
def print_verbose(line):
    """Print only when verbose and non-silent"""
    line = add_timestamp(line)
    if (not get_args().silent) and get_args().verbose:
        write_to_logfile(line)
        return __builtin__.print(line)

def print_timestamp_only():
    """Prints just the current timestamp to dev console"""
    return __builtin__.print(get_current_time().strftime('%H:%M:%S'))

def print_start_message():
    """Prints start message"""
    print(f'Starting {get_args().mode} lighting')

def print_sigint_message():
    """Prints end message on SIGINT event"""
    print(f'Ending {get_args().mode} lighting on SIGINT')

def print_end_message():
    """Prints end message"""
    print(f'Ending {get_args().mode} lighting')