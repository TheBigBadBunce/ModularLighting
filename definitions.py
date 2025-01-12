import json
from datetime import time
from arguments import get_args
from devices import OutputDevice, InputDevice
from schedules import AlwaysOnSchedule, ConsistentDailySchedule, ConsistentDimmedDailySchedule
from timeutils import parse_time

def create_device(definition):
    if definition["type"] == "output":
        device = OutputDevice(definition["pin"], definition["location"])
        try: device.min_level = definition["min_level"]
        except KeyError: pass
        try: device.max_level = definition["max_level"]
        except KeyError: pass
    elif definition["type"] == "input":
        device = InputDevice(definition["pin"])
    else:
        raise NotImplementedError
    return device
    
def create_schedule(device, definition):
    if definition["type"] == "always on":
        return AlwaysOnSchedule(device)
    elif definition["type"] == "consistent daily":
        schedule = ConsistentDailySchedule(
            parse_time(definition["start_time"]),
            parse_time(definition["end_time"]),
            device
        )
        try: schedule.variance = definition["variance"]
        except KeyError: pass
        return schedule
    elif definition["type"] == "consistent daily dimmed":
        return ConsistentDimmedDailySchedule(
            parse_time(definition["start_time"]), 
            parse_time(definition["end_time"]),
            definition["dim_up_time"],
            definition["dim_down_time"],
            device
        )
    else:
        raise NotImplementedError


def define_devices_schedules_events():
    """Defines every device in the city, as well as load schedules and create events"""

    all_output_devices = []
    all_input_devices = [] # Possibility of having multiple inputs later, hence array
    all_schedules = []
    all_events = []

    with open(get_args().definitions, "r") as def_file:
        definitions = json.load(def_file)
        for event_def in definitions:
            device = create_device(event_def)

            if event_def["type"] == "output":
                all_output_devices.append(device)
                for schedule_def in event_def["schedules"]:
                    schedule = create_schedule(device, schedule_def)
                    all_schedules.append(schedule)
            elif event_def["type"] == "input":
                all_input_devices.append(device)

    for schedule in all_schedules:
        all_events += schedule.generate_events()

    return [all_output_devices, all_input_devices, all_events]