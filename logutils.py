import builtins as __builtin__
from pprint import pprint
from timeutils import get_current_time
from constants import LOGFILE_REALTIME, LOGFILE_SIMULATE, LOGFILE_FULL
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
    elif time_emulation == "full":
        return LOGFILE_FULL
    else:
        raise NotImplementedError("No logfile exists for this mode")

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

def print(line, pretty=False):
    """Print under normal (non-silent) circumstances"""
    if not get_args().silent:
        if pretty:
            return pprint(line)
        line = add_timestamp(str(line))
        write_to_logfile(line)
        return __builtin__.print(line)
    
def print_verbose(line, pretty=False):
    """Print only when verbose and non-silent"""
    if  get_args().verbose:
        print(line, pretty)

def print_timestamp_only():
    """Prints just the current timestamp to dev console"""
    if not get_args().silent:
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

def debug_print_devices_events(output_devices, input_devices, events):
    __builtin__.print()
    print_verbose(f'Parsed output devices:')
    print_verbose(output_devices, pretty=True)
    __builtin__.print()
    print_verbose(f'Parsed input devices:')
    print_verbose(input_devices, pretty=True)
    __builtin__.print()
    print_verbose(f'Generated events:')
    print_verbose(events, pretty=True)
    __builtin__.print()