from datetime import time
from devices import Device
from schedules import ConsistentDailySchedule

def load_all_events():
    device = Device(1, "Coffee shop")
    schedule = ConsistentDailySchedule(time(5),time(9), device)
    events = schedule.generate_events()

    return events