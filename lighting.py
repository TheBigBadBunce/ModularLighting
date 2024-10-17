from datetime import time
from timeutils import increase_simulated_time, get_time_emulation
from time import sleep
from devices import Device
from schedules import *
from arguments import parse_arguments
from logging import print_start_and_sigint_message, print_end_message, print_timestamp_only, set_silent, set_verbose, reset_logfile

set_silent(False)
set_verbose(True)

(
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

if get_time_emulation() == 'simulated':
    reset_logfile()
    print_start_and_sigint_message()
    i = 0
    while(i < (1440 / time_simulation_increment) +1):
        print_timestamp_only()
        handle_events_since_last_cycle()
        increase_simulated_time(time_simulation_increment)
        sleep(0.5)
        i += 1

else: # 'realtime' or 'offset'
    i = 0
    print_start_and_sigint_message()
    while(True):
        print_timestamp_only()
        handle_events_since_last_cycle()
        sleep(1)

print_end_message()