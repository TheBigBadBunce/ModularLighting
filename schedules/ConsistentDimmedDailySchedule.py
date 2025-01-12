from datetime import time
from events import DimOnEvent, DimOffEvent
from timeutils import time_to_string
from . import ConsistentDailySchedule
        
class ConsistentDimmedDailySchedule(ConsistentDailySchedule):
    """A fixed period when a single device is on, with dim up/down times"""
    dim_up_time = 0
    dim_down_time = 0
    device = None

    def generate_events(self):
        return [
            DimOnEvent(self.start_time, self.dim_up_time, self.device),
            DimOffEvent(self.end_time, self.dim_down_time, self.device)
        ]

    def __init__(self, start_time, end_time, dim_up_time, dim_down_time, device):
        super().__init__(start_time, end_time, device)
        self.dim_up_time = dim_up_time
        self.dim_down_time = dim_down_time

    def get_debug_info(self):
        return f"{super().get_debug_info()}, {self.dim_up_time}s/{self.dim_down_time}s"