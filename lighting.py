from datetime import time
from timeutils import increase_simulated_time, get_simulated_time, get_current_time
from time import sleep
from devices import Device
from schedules import *
from arguments import parse_arguments
from logging import print, print_verbose, set_silent, set_verbose

set_silent(False)
set_verbose(True)

"""Core process of lighting app"""

(
    time_emulation,
    time_simulation_increment,
) = parse_arguments()

device = Device(1, "Coffee shop")
schedule = ConsistentDailySchedule(time(5),time(9), device)
events = schedule.generate_events()

def handle_events_since_last_cycle():
    events_for_deletion = []
    for event in events:
        event.handle_event()
        if event.ready_for_deletion():
            events_for_deletion.append(event)

    for event in events_for_deletion:
        events.remove(event)

if time_emulation == 'simulated':
    i = 0
    while(i < (1440 / time_simulation_increment) +1):
        print(get_current_time().strftime("%H:%M:%S"))
        handle_events_since_last_cycle()
        increase_simulated_time(time_simulation_increment)
        sleep(0.5)
        i += 1

else: # 'realtime' or 'offset'
    i = 0
    while(True):
        handle_events_since_last_cycle()
        print(get_current_time().strftime("%H:%M:%S"))
        sleep(1)
