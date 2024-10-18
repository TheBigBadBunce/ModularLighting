from datetime import time
from devices import Device
from schedules import ConsistentDailySchedule

def define_devices_schedules_events():
    """Defines every device in the city, as well as load schedules and create events"""
    # TODO load these from a file / variable
    device = Device(17, "Coffee shop")
    device.setup()
    schedule = ConsistentDailySchedule(time(5),time(9), device)
    events = schedule.generate_events()

    return events