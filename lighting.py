import threading
from timeutils import increase_simulated_time, get_time_emulation
from time import sleep
from schedules import *
from arguments import parse_arguments
from logging import print_start_message, print_end_message, print_timestamp_only, set_silent, set_verbose, reset_logfile, get_tick_printouts
from definitions import define_output_devices_schedules_events, define_input_devices
from ioutils import initialise_GPIO, close_GPIO
from dimutils import get_dim, set_dim
from constants import SIMULATION_TICKS_PER_SECOND, DIM_DROPOFF_PER_TICK

set_silent(False)
set_verbose(True)

set_dim(100) # 0-100 for PWM percentage

( time_simulation_increment, ) = parse_arguments()

initialise_GPIO()
[output_devices, events] = define_output_devices_schedules_events()
[pir] = define_input_devices()

def update_dim_and_outputs(new_dim):
    set_dim(new_dim)
    for device in output_devices:
        device.update_output()

def handle_events_since_last_cycle():
    events_for_deletion = []
    event_threads = []
    for event in events:
        event_threads.append(threading.Thread(target=event.handle_event))
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
    while(i < ((1440 / time_simulation_increment) * SIMULATION_TICKS_PER_SECOND) +1):
        print_timestamp_only()
        handle_events_since_last_cycle()
        increase_simulated_time(int(time_simulation_increment / SIMULATION_TICKS_PER_SECOND))
        sleep(1 / SIMULATION_TICKS_PER_SECOND)
        i += 1

else: # 'realtime' or 'offset'
    i = 0
    print_start_message()
    while(True):
        pir_value = pir.get_level()
        dim_value = get_dim()
        if dim_value > 0 and pir_value == 0:
            update_dim_and_outputs(dim_value - DIM_DROPOFF_PER_TICK)
        if dim_value < 100 and pir_value == 1:
            update_dim_and_outputs(100)

        if get_tick_printouts():
            print_timestamp_only()
        handle_events_since_last_cycle()
        sleep(0.1)

print_end_message()
close_GPIO()