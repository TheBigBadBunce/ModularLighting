import configargparse
from datetime import time, datetime, timedelta
import timeutils

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

    parser = configargparse.ArgumentParser(
        prog='Modular City lighting',
        description='Controls and simulates lighting for my lego modular city.',
        default_config_files=['./lighting.conf', './lighting.yaml'],
        formatter_class=configargparse.ArgumentDefaultsRawHelpFormatter)
    
    parser.add('-c', '--config', is_config_file=True, help='config file path')

    parser.add('-m', '--mode', default="realtime", type=str, help='Lighting mode. See README.md!')
    parser.add('-o', '--offset', default="0", type=str, help='Realtime mode only: time difference from current.')
    parser.add('-i', '--interval', default=60, type=int, help='Simulate mode only: Interval between simulation ticks. Equal to minutes simulated per second.')

    parser.add('-p', '--pir', default=False, action='store_true', help='Use a PIR sensor (defined in `definitions.py`) to slowly dim lights to 0 when no movement is detected.')
    parser.add('-v', '--verbose', default=False, action='store_true', help='Enable verbose debug output')
    parser.add('-t', '--tick_printouts', default=False, action='store_true', help='Print/log a timestamp every tick. Ignores other log settings (except silent).')
    parser.add('-s', '--silent', default=False, action='store_true', help='Remove all console output. Especially useful for running in the background. Overrides `verbose`.')
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