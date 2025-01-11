from timeutils import time_is_in_past, time_to_string
from . import Event

class SimpleEvent(Event):
    """Events with a single one-time adjustment"""

    def handle_event(self):
        raise NotImplementedError()
    
    def ready_for_deletion(self):
        return time_is_in_past(self.event_time)

    def get_debug_info(self):
        return time_to_string(self.event_time)

class TurnOnEvent(SimpleEvent):
    """Turns a single device to max"""
    def handle_event(self):
        if time_is_in_past(self.event_time):
            self.device.set_max()

class TurnOffEvent(SimpleEvent):
    """Turns a single device to min"""
    def handle_event(self):
        if time_is_in_past(self.event_time):
            self.device.set_min()