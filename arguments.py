import configargparse
import timeutils # avoid circular import
from datetime import timedelta, datetime
from constants import DAILY_RESET_TIME

def parse_time_offset(new_offset):
    """Parses time offset for offset mode from argument string"""

    negative = False
    if new_offset.startswith('-'):
        negative = True
        new_offset = new_offset[1:]
    offset = timeutils.parse_time(new_offset)
    time_offset = timedelta(hours=offset.hour, minutes=offset.minute)
    
    if negative:
        time_offset = -time_offset

    return time_offset


def parse_arguments():
    """Parse all command line arguments and return options as appropriate"""

    parser = configargparse.ArgumentParser(
        prog='Modular City lighting',
        description='Controls and simulates lighting for my lego modular city.',
        default_config_files=['./lighting.conf', './lighting.yaml'],
        formatter_class=configargparse.ArgumentDefaultsRawHelpFormatter,
        epilog="More detailed information can be found under docs/ or at https://github.com/TheBigBadBunce/ModularLighting"
    )
    
    parser.add('-c', '--config', is_config_file=True, help='config file path')
    parser.add('-d', '--definitions', default='./definitions.json', help='device/schedule definition file path')

    parser.add('-m', '--mode', default="realtime", type=str, help='lighting mode')
    parser.add('-o', '--offset', default="0", type=str, help='time difference from current (realtime only)')
    parser.add('-i', '--interval', default=60, type=int, help='interval between simulation ticks (simulate only)')

    parser.add('-p', '--pir', default=False, action='store_true', help='use a PIR sensor to dim lights when no movement is detected')
    parser.add('-v', '--verbose', default=False, action='store_true', help='verbose debug output')
    parser.add('-t', '--tick_printouts', default=False, action='store_true', help='print/log a timestamp every tick')
    parser.add('-s', '--silent', default=False, action='store_true', help='remove all console output')
    args = parser.parse_args()

    args.offset = parse_time_offset(args.offset)
    set_args(args)

    if args.mode == "simulate":
        timeutils.set_simulated_time(datetime.combine(datetime.today(), DAILY_RESET_TIME))
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