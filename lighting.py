import threading
from pir import check_pir
from timeutils import increase_simulated_time, time_is_in_past
from time import sleep
from schedules import *
from arguments import parse_arguments, get_args
from logutils import print_start_message, print_end_message, print_timestamp_only, reset_logfile, debug_print_devices_events
from definitions import define_devices_schedules_events
from ioutils import initialise_GPIO, close_GPIO
from dimutils import set_dim
from constants import SIMULATION_TICKS_PER_SECOND

set_dim(1)

parse_arguments()

initialise_GPIO()
[output_devices, input_devices, events] = define_devices_schedules_events()
[pir] = input_devices

debug_print_devices_events(output_devices, input_devices, events) # sort

def handle_events_since_last_cycle():
    events_for_deletion = []
    event_threads = []
    for event in events:
        if time_is_in_past(event.event_time):
            event_threads.append(threading.Thread(target=event.handle_event))
            events_for_deletion.append(event)

    for event in events_for_deletion:
        events.remove(event)

    # Wait for all events to resolve
    for event_thread in event_threads:
        event_thread.start()
        event_thread.join()

mode = get_args().mode

if mode == 'simulate':
    reset_logfile()
    print_start_message()
    i = 0
    while(i < ((1440 / get_args().interval) * SIMULATION_TICKS_PER_SECOND)):
        print_timestamp_only()
        handle_events_since_last_cycle()
        increase_simulated_time(int(get_args().interval / SIMULATION_TICKS_PER_SECOND))
        sleep(1 / SIMULATION_TICKS_PER_SECOND)
        i += 1

elif mode == 'realtime':
    i = 0
    print_start_message()
    while(True):
        if (get_args().pir):
            check_pir(pir, output_devices)

        if get_args().tick_printouts:
            print_timestamp_only()
        handle_events_since_last_cycle()
        sleep(0.1)

else: # 'full'
    for device in output_devices:
        device.set_max()
    while (True):
        pass

print_end_message()
close_GPIO()