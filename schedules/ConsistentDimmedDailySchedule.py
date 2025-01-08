from datetime import time
from events import DimOnEvent, DimOffEvent
from timeutils import time_to_string
from . import Schedule
        
class ConsistentDimmedDailySchedule(Schedule):
    """A fixed period when a single device is on, with dim up/down times"""
    start_time = time(00,00)
    end_time = time(23,59)
    dim_up_time = 0
    dim_down_time = 0
    device = None

    def generate_events(self):
        return [
            DimOnEvent(self.start_time, self.device),
            DimOffEvent(self.end_time, self.device)
        ]

    def __init__(self, start_time, end_time, device):
        super().__init__()
        self.start_time = start_time
        self.end_time = end_time
        self.device = device

    def get_debug_info(self):
        return f"{time_to_string(self.start_time)}-{time_to_string(self.end_time)}, {self.dim_up_time}s/{self.dim_down_time}s"