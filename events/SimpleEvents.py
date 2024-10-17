from constants import GPIO_PIN_MAX, GPIO_PIN_MIN
from timeutils import time_is_in_past, print_time
from . import Event

class SimpleEvent(Event):
    def handle_event(self):
        raise NotImplementedError()
    
    def ready_for_deletion(self):
        return time_is_in_past(self.event_time)

    def get_debug_info(self):
        return print_time(self.event_time)

class TurnOnEvent(SimpleEvent):
    def handle_event(self):
        if time_is_in_past(self.event_time):
            self.device.set_gpio_pin(GPIO_PIN_MAX)

class TurnOffEvent(SimpleEvent):
    def handle_event(self):
        if time_is_in_past(self.event_time):
            self.device.set_gpio_pin(GPIO_PIN_MIN)