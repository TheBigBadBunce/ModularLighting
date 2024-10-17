from logging import print

class Device():
    """A single LED"""
    gpio_pin = None
    location = ""

    def set_gpio_pin(self, value):
        """Set the power(?) on the device's GPIO pin"""
        # TODO
        print(f"Setting {self.location} to {value}")
        pass

    def __init__(self, gpio_pin, location):
        super().__init__()
        self.gpio_pin = gpio_pin
        self.location = location   