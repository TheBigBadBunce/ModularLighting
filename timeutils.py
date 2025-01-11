from datetime import date, datetime, time, timedelta

from arguments import get_args

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

    new_hours = simulated_time.hour
    new_minutes = simulated_time.minute + increase_minutes
    while new_minutes >= 60:
        new_minutes -= 60
        new_hours += 1
    while new_hours >= 24:
        new_hours = new_hours - 24
    
    simulated_time = time(new_hours, new_minutes)

def get_simulated_time():
    """Getter for simulated time"""
    global simulated_time
    return simulated_time

def get_current_time():
    """Getter for current time in emulation"""
    if get_args().mode == "realtime":
        return (datetime.now() + get_args().offset).time()
    else:
        return simulated_time
    
def time_is_in_past(time, extra_seconds = 0):
    """Returns whether a time is in the past, within the current time emulation"""
    if get_args().mode == "realtime":
        current_time = get_current_time()
    else:
        current_time = simulated_time

    dt_time = datetime.combine(date.today(), time) + timedelta(seconds=extra_seconds)
    dt_current = datetime.combine(date.today(), current_time)
    return dt_time <= dt_current