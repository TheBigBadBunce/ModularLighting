from timeutils import time_is_in_past, time_to_string
from . import Event

class DimEvent(Event):
    """Events with a single linear dim on/off"""

    dim_time = 0

    def handle_event(self):
        raise NotImplementedError()
    
    def ready_for_deletion(self):
        return time_is_in_past(self.event_time, extra_seconds=self.dim_time)

    def get_debug_info(self):
        return f"{self.device.location} {time_to_string(self.event_time)} / {self.dim_time}s"
    
    def __init__(self, event_time, dim_time, device):
        self.dim_time = dim_time
        super().__init__(event_time, device)

class DimOnEvent(DimEvent):
    """Dims a single device to max"""
    def handle_event(self):
        self.device.dim_level(1, self.dim_time)

class DimOffEvent(DimEvent):
    """Dims a single device to min"""
    def handle_event(self):
        self.device.dim_level(0, self.dim_time)