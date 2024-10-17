from datetime import datetime, time, timedelta

def print_time(time):
    return time.isoformat(timespec="minutes")

def set_time_offset(new_offset):
    global time_offset

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

def set_time_emulation(new_emulation):
    global time_emulation
    time_emulation = new_emulation

def set_simulated_time(new_time):
    global simulated_time
    simulated_time = new_time

def increase_simulated_time(increase_minutes):
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
    global simulated_time
    return simulated_time

def get_current_time():
    global time_offset
    offset_time = datetime.now() + time_offset
    return offset_time.time().strftime("%H:%M:%S")

def time_is_in_past(time):
    if time_emulation == "realtime":
        current_time = datetime.now().time()
    else:
        current_time = simulated_time
    return time <= current_time