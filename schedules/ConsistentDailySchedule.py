from datetime import time
from events import TurnOnEvent, TurnOffEvent
from timeutils import time_to_string
from . import Schedule
        
class ConsistentDailySchedule(Schedule):
    """A fixed period when a single device is on"""
    start_time = time(00,00)
    end_time = time(23,59)
    device = None

    def generate_events(self):
        return [
            TurnOnEvent(self.start_time, self.device),
            TurnOffEvent(self.end_time, self.device)
        ]

    def __init__(self, start_time, end_time, device):
        super().__init__()
        self.start_time = start_time
        self.end_time = end_time
        self.device = device

    def get_debug_info(self):
        return f"{time_to_string(self.start_time)}-{time_to_string(self.end_time)}"