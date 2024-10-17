import signal
import sys
import builtins as __builtin__

from timeutils import get_current_time, get_time_emulation
from constants import LOGFILE_REALTIME, LOGFILE_OFFSET, LOGFILE_SIMULATE

def set_verbose(new_verbose):
    """Setter for verbose logging"""
    global verbose
    verbose = new_verbose

def set_silent(new_silent):
    """Setter to silence logging"""
    global silent
    silent = new_silent

def add_timestamp(line):
    """Adds timestamp to output"""
    return get_current_time().strftime('%H:%M:%S') + " ~ " + line

def get_logfile_name():
    time_emulation = get_time_emulation()
    if time_emulation == "realtime":
        return LOGFILE_REALTIME
    elif time_emulation == "offset":
        return LOGFILE_OFFSET
    elif time_emulation == "simulated":
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
    """Resets logfile to empty, USE WITH CAUTION! Intended use case: clear logfile before simulated lighting"""
    file = open(get_logfile_name(), "w")
    file.write("")
    file.close()

def print(line):
    """Print under normal (non-silent) circumstances"""
    global silent

    line = add_timestamp(line)
    if not silent:
        write_to_logfile(line)
        return __builtin__.print(line)
    
def print_verbose(line):
    """Print only when verbose and non-silent"""
    global silent
    global verbose

    line = add_timestamp(line)
    if (not silent) and verbose:
        write_to_logfile(line)
        return __builtin__.print(line)

def print_timestamp_only():
    """Prints just the current timestamp to dev console"""
    return __builtin__.print(get_current_time().strftime('%H:%M:%S'))

def print_start_and_sigint_message():
    """Prints start message and primes SIGINT event"""
    print(f'Starting {get_time_emulation()} lighting')

    def signal_handler(sig, frame):
        print(f'Ending {get_time_emulation()} lighting on SIGINT')
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

def print_end_message():
    """Prints end message"""
    print(f'Ending {get_time_emulation()} lighting')