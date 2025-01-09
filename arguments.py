import argparse
from datetime import time
from timeutils import set_time_emulation, set_simulated_time, set_time_offset
from schedules import *
from logging import set_silent, set_verbose, set_tick_printouts

def parse_arguments():
    """Parse all command line arguments and return options as appropriate"""
    parser = argparse.ArgumentParser(
        prog='Modular City lighting',
        description='Controls and simulates lighting for my lego modular city')
    parser.add_argument('--simulate', default=None, type=int)
    parser.add_argument('--realtime', default=False, action='store_true')
    parser.add_argument('--offset', default="0", type=str)
    parser.add_argument('--verbose', default=False, action='store_true')
    parser.add_argument('--tick_printouts', default=False, action='store_true')
    parser.add_argument('--silent', default=False, action='store_true')
    args = parser.parse_args()

    set_silent(args.silent)
    set_verbose(args.verbose)
    set_tick_printouts(args.tick_printouts)

    run_modes_given = (args.simulate is not None) + (args.realtime) + (args.offset != "0")

    if (run_modes_given != 1):
        raise ValueError("Must be run with ONE of --realtime, --offset, or --simulate!")

    time_emulation = None
    if args.realtime:
        time_emulation = "realtime"

    elif args.offset != "0":
        time_emulation = "offset"

    elif args.simulate is not None:
        time_emulation = "simulated"
        set_simulated_time(time(0))
        if args.simulate <= 0:
            raise ValueError("Simulation interval must be positive")
        if args.simulate > 480:
            raise ValueError("Simulation interval over 8 hours is too high to test")
        
    else:
        raise NotImplementedError("Invalid time emulation selected")

    set_time_emulation(time_emulation)
    set_time_offset(args.offset)

    return (args.simulate,)