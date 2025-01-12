from datetime import date, datetime, time, timedelta
from arguments import get_args

def parse_time(string):
    """Parse time string into datetime"""

    try:
        parsed_datetime = datetime.combine(datetime.today(), datetime.strptime(string, "%H:%M:%S").time())
    except ValueError:
        try:
            parsed_datetime = datetime.combine(datetime.today(), datetime.strptime(string, "%H:%M").time())
        except ValueError:
            parsed_datetime = datetime.combine(datetime.today(), datetime.strptime(string, "%M").time())

    if parsed_datetime.hour < 4:
        parsed_datetime += timedelta(days=1)

    return parsed_datetime

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
    
def time_is_in_past(dt, extra_seconds = 0):
    """Returns whether a datetime is in the past, within the current time emulation"""
    if get_args().mode == "realtime":
        current_time = get_current_time()
    else:
        current_time = simulated_time

    return dt + timedelta(seconds=extra_seconds) <= current_time