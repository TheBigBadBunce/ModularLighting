class Schedule():
    def generate_events(self):
        raise NotImplementedError()

    def __str__(self):
        string = f"<{self.__class__.__name__} "
        string += self.get_debug_info()
        string += ">"
        return string

    def __repr__(self):
        return self.__str__()
    
    def get_debug_info(self):
        if (self.__class__.__name__ != 'Schedule'):
            raise NotImplementedError() 
        return "WARNING BASE SCHEDULE"