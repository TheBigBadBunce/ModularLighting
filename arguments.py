import argparse

from datetime import time
from timeutils import set_time_emulation, set_simulated_time, set_time_offset
from schedules import *
from logging import set_silent, set_verbose

def parse_arguments():
    """Parse all command line arguments and return options as appropriate"""
    parser = argparse.ArgumentParser(
        prog='Modular City lighting',
        description='Controls and simulates lighting for my lego modular city')
    parser.add_argument('--simulate', default=None, type=int)
    parser.add_argument('--realtime', default=False, action='store_true')
    parser.add_argument('--offset', default="0", type=str)
    parser.add_argument('--verbose', default=False, action='store_true')
    parser.add_argument('--silent', default=False, action='store_true')
    args = parser.parse_args()

    set_silent(args.silent)
    set_verbose(args.verbose)

    run_modes_given = (args.simulate is not None) + (args.realtime) + (args.offset != "0")

    if (run_modes_given != 1):
        raise ValueError("Must be run with ONE of --realtime, --offset, or --simulate!")


    set_time_offset(args.offset)

    time_emulation = None
    if args.realtime:
        time_emulation = "realtime"
        set_time_emulation("realtime")

    elif args.offset != "0":
        time_emulation = "offset"
        set_time_emulation("realtime")

    elif args.simulate is not None:
        time_emulation = "simulated"
        set_time_emulation("simulated")
        set_simulated_time(time(0))
        if args.simulate <= 0:
            raise ValueError("Simulation interval must be positive")
        if args.simulate > 480:
            raise ValueError("Simulation interval over 8 hours is too high to test")
        
    else:
        raise NotImplementedError("Invalid time emulation selected")

    return (time_emulation, args.simulate)