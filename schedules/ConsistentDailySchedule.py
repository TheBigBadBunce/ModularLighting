from datetime import time
from events import TurnOnEvent, TurnOffEvent
from timeutils import time_to_string
from randomutils import vary_time
from . import Schedule
        
class ConsistentDailySchedule(Schedule):
    """A fixed period when a single device is on"""
    start_time = time(00,00)
    end_time = time(23,59)
    device = None
    variance = 0

    def generate_events(self):
        start_time = vary_time(self.start_time, self.variance)
        end_time = vary_time(self.end_time, self.variance)
        return [
            TurnOnEvent(start_time, self.device),
            TurnOffEvent(end_time, self.device)
        ]

    def __init__(self, start_time, end_time, device):
        super().__init__()
        self.start_time = start_time
        self.end_time = end_time
        self.device = device

    def get_debug_info(self):
        return f"{time_to_string(self.start_time)}-{time_to_string(self.end_time)}"