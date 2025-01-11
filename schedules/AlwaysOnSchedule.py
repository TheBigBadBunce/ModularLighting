from datetime import time
from events import TurnOnEvent
from timeutils import time_to_string
from . import Schedule
        
class AlwaysOnSchedule(Schedule):
    """Device is always on"""
    device = None

    def generate_events(self):
        return [TurnOnEvent(time(0, 0), self.device)]

    def __init__(self, device):
        super().__init__()
        self.device = device

    def get_debug_info(self):
        return ""