from datetime import time
from timeutils import increase_simulated_time, get_simulated_time, get_current_time
from time import sleep
from devices import Device
from schedules import *
from arguments import parse_arguments

(
    time_emulation,
    time_simulation_increment,
    verbose,
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
        print(get_simulated_time().strftime('%H:%M'))
        handle_events_since_last_cycle()
        increase_simulated_time(time_simulation_increment)
        sleep(0.5)
        i += 1

else: # 'realtime' or 'offset'
    i = 0
    while(True):
        handle_events_since_last_cycle()
        print(get_current_time())
        sleep(1)
