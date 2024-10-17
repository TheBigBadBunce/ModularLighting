from datetime import time

class Event():
    event_time = time(0,00)
    device = None

    def handle_event(current_time):
        raise NotImplementedError()

    def ready_for_deletion(current_time):
        raise NotImplementedError()

    def __init__(self, event_time, device):
        super().__init__()
        self.event_time = event_time
        self.device = device

    def __str__(self):
        string = f"<{self.__class__.__name__} "
        string += self.get_debug_info()
        string += ">"
        return string
    
    def __repr__(self):
        return self.__str__()
    
    def get_debug_info(self):
        if (self.__class__.__name__ != 'Event'):
            raise NotImplementedError()
        return "WARNING BASE EVENT"