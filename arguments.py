import argparse
from datetime import time, datetime, timedelta
from enum import Enum
import timeutils
from typing import Literal

def parse_time_offset(new_offset):
    """Parses time offset for offset mode from argument string"""

    negative = False
    if new_offset.startswith('-'):
        negative = True
        new_offset = new_offset[1:]
    try:
        parsed_datetime = datetime.strptime(new_offset, "%H:%M:%S")
    except ValueError:
        try:
            parsed_datetime = datetime.strptime(new_offset, "%H:%M")
        except ValueError:
            parsed_datetime = datetime.strptime(new_offset, "%M")
    time_offset = timedelta(hours=parsed_datetime.hour, minutes=parsed_datetime.minute)
    
    if negative:
        time_offset = -time_offset

    return time_offset


def parse_arguments():
    """Parse all command line arguments and return options as appropriate"""
    parser = argparse.ArgumentParser(
        prog='Modular City lighting',
        description='Controls and simulates lighting for my lego modular city')
    
    parser.add_argument('--mode', default="realtime", type=str)
    parser.add_argument('--offset', default="0", type=str)
    parser.add_argument('--interval', default=60, type=int)

    parser.add_argument('--pir', default=False, action='store_true')
    parser.add_argument('--verbose', default=False, action='store_true')
    parser.add_argument('--tick_printouts', default=False, action='store_true')
    parser.add_argument('--silent', default=False, action='store_true')
    args = parser.parse_args()

    args.offset = parse_time_offset(args.offset)
    set_args(args)

    if args.mode == "simulate":
        timeutils.set_simulated_time(time(0))
        if args.interval <= 0:
            raise ValueError("Simulation interval must be positive")
        if args.interval > 480:
            raise ValueError("Simulation interval over 8 hours is too high to test")
    elif args.mode not in ["realtime", "full"]:
        raise NotImplementedError("Invalid time emulation selected")

def set_args(args):
    """Store arguments for access from elsewhere"""
    global arguments
    arguments = args

def get_args():
    """Return args namespace (kw lookup wasn't friendly :()"""
    global arguments
    return arguments