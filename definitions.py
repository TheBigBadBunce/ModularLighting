from datetime import time
from devices import Device
from schedules import ConsistentDailySchedule

def define_devices_schedules_events():
    """Defines every device in the city, as well as load schedules and create events"""

    all_devices = []
    all_schedules = []
    all_events = []

    hotel_art_shop = Device(26, "Art shop")
    all_schedules.append(ConsistentDailySchedule(time(9),time(19), hotel_art_shop))

    hotel_lobby = Device(19, "Hotel Lobby")
    all_schedules.append(ConsistentDailySchedule(time(5),time(23,59), hotel_lobby))

    hotel_room_11 = Device(13, "Hotel room 11")
    all_schedules.append(ConsistentDailySchedule(time(7),time(8), hotel_room_11))
    all_schedules.append(ConsistentDailySchedule(time(22),time(23,30), hotel_room_11))

    hotel_room_12 = Device(6, "Hotel room 12")
    all_schedules.append(ConsistentDailySchedule(time(6,30),time(8,30), hotel_room_12))
    all_schedules.append(ConsistentDailySchedule(time(18),time(21), hotel_room_12))

    hotel_room_21 = Device(5, "Hotel room 21")
    all_schedules.append(ConsistentDailySchedule(time(10),time(20), hotel_room_21))

    all_devices += [hotel_art_shop, hotel_lobby, hotel_lobby, hotel_room_11, hotel_room_12, hotel_room_21]

    # TODO load these from a file / variable
    for device in all_devices:
        device.setup()
    for schedule in all_schedules:
        all_events += schedule.generate_events()

    return all_events