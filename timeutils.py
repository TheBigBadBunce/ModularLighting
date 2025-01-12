from datetime import date, datetime, time, timedelta
from arguments import get_args

def parse_time(string):
    """Parse time string into tuple (hours, minutes)"""

    try:
        parsed_datetime = datetime.strptime(string, "%H:%M:%S")
    except ValueError:
        try:
            parsed_datetime = datetime.strptime(string, "%H:%M")
        except ValueError:
            parsed_datetime = datetime.strptime(string, "%M")

    return time(parsed_datetime.hour, parsed_datetime.minute)

def time_to_string(time):
    """Converts a `time` to readable string"""
    return time.isoformat(timespec="minutes")

def set_simulated_time(new_time):
    """Set/update the simulated time"""
    global simulated_time
    simulated_time = new_time

def increase_simulated_time(increase_minutes):
    """Move the simulated time forward by increase_minutes"""
    global simulated_time
    simulated_time += timedelta(minutes=increase_minutes)

def get_simulated_time():
    """Getter for simulated time"""
    global simulated_time
    return simulated_time

def get_current_time():
    """Getter for current time in emulation"""
    if get_args().mode == 'simulate':
        return simulated_time
    else:
        return datetime.now() + get_args().offset
    
def time_is_in_past(time, extra_seconds = 0):
    """Returns whether a time is in the past, within the current time emulation"""
    if get_args().mode == "realtime":
        current_time = get_current_time()
    else:
        current_time = simulated_time

    dt_time = datetime.combine(date.today(), time) + timedelta(seconds=extra_seconds)
    return dt_time <= current_time