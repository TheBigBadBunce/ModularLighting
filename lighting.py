import threading
from timeutils import increase_simulated_time, get_time_emulation
from time import sleep
from schedules import *
from arguments import parse_arguments
from logging import print_start_message, print_end_message, print_timestamp_only, set_silent, set_verbose, reset_logfile
from definitions import define_devices_schedules_events
from ioutils import initialise_GPIO, close_GPIO
from constants import SIMULATION_PINGS_PER_SECOND

set_silent(False)
set_verbose(True)

( time_simulation_increment, ) = parse_arguments()

initialise_GPIO()
events = define_devices_schedules_events()

def handle_events_since_last_cycle():
    events_for_deletion = []
    event_threads = []
    for event in events:
        event_threads.append(threading.Thread(target=event.handle_event))
        event.handle_event()
        if event.ready_for_deletion():
            events_for_deletion.append(event)

    for event in events_for_deletion:
        events.remove(event)

    # Wait for all events to resolve
    for event_thread in event_threads:
        event_thread.start()
        event_thread.join()

if get_time_emulation() == 'simulated':
    reset_logfile()
    print_start_message()
    i = 0
    while(i < ((1440 / time_simulation_increment) * SIMULATION_PINGS_PER_SECOND) +1):
        print_timestamp_only()
        handle_events_since_last_cycle()
        increase_simulated_time(int(time_simulation_increment / SIMULATION_PINGS_PER_SECOND))
        sleep(1 / SIMULATION_PINGS_PER_SECOND)
        i += 1

else: # 'realtime' or 'offset'
    i = 0
    print_start_message()
    while(True):
        print_timestamp_only()
        handle_events_since_last_cycle()
        sleep(1)

print_end_message()
close_GPIO()