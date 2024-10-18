from logging import print
from ioutils import setup_led, set_GPIO_pin

class Device():
    """A single LED"""
    gpio_pin = None
    location = ""

    def set_gpio_pin(self, value):
        """Set the power(?) on the device's GPIO pin"""
        print(f"Setting {self.location} to {value}")
        set_GPIO_pin(self.gpio_pin, value)
        pass

    def setup(self):
        """Initialise the device"""
        setup_led(self.gpio_pin)

    def __init__(self, gpio_pin, location):
        super().__init__()
        self.gpio_pin = gpio_pin
        self.location = location   