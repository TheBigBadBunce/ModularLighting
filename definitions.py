from datetime import time
from devices import OutputDevice, InputDevice
from schedules import ConsistentDailySchedule

def define_output_devices_schedules_events():
    """Defines every device in the city, as well as load schedules and create events"""

    all_output_devices = []
    all_schedules = []
    all_events = []

    hotel_art_shop = OutputDevice(26, "Art shop")
    all_schedules.append(ConsistentDailySchedule(time(9),time(19), hotel_art_shop))
    all_output_devices.append(hotel_art_shop)

    hotel_lobby = OutputDevice(19, "Hotel Lobby")
    all_schedules.append(ConsistentDailySchedule(time(5),time(23,59), hotel_lobby))
    all_output_devices.append(hotel_lobby)

    hotel_room_11 = OutputDevice(13, "Hotel room 11")
    all_schedules.append(ConsistentDailySchedule(time(7),time(8), hotel_room_11))
    all_schedules.append(ConsistentDailySchedule(time(22),time(23,30), hotel_room_11))
    all_output_devices.append(hotel_room_11)

    hotel_room_12 = OutputDevice(6, "Hotel room 12")
    all_schedules.append(ConsistentDailySchedule(time(6,30),time(8,30), hotel_room_12))
    all_schedules.append(ConsistentDailySchedule(time(18),time(21), hotel_room_12))
    all_output_devices.append(hotel_room_12)

    hotel_room_21 = OutputDevice(5, "Hotel room 21")
    all_schedules.append(ConsistentDailySchedule(time(10),time(20), hotel_room_21))
    all_output_devices.append(hotel_room_21)

    # TODO load these from a file / variable

    for schedule in all_schedules:
        all_events += schedule.generate_events()

    return [all_output_devices, all_events]

def define_input_devices():
    """Defines input devices"""

    # TODO also get this from a file
    # TODO throw an error on startup if this is None and pir is specified
    pir = InputDevice(11)

    # Possibility of having multiple inputs later, hence array
    return [pir]

