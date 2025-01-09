from logging import print
from dimutils import get_dim
from ioutils import setup_led, create_pwm

class Device():
    """A single LED"""
    gpio_pin = None
    pwm = None
    location = ""
    level = 0

    def update_output(self):
        global_dim = get_dim()
        self.pwm.ChangeDutyCycle(self.level * global_dim)

    def set_level(self, value):
        """Set the power(?) on the device's GPIO pin"""
        print(f"Setting {self.location} to {value}")
        self.level = value
        self.update_output()

    def setup(self):
        """Initialise the device"""
        setup_led(self.gpio_pin)
        self.pwm = create_pwm(self.gpio_pin)
        self.pwm.start(self.level)

    def __init__(self, gpio_pin, location):
        super().__init__()
        self.gpio_pin = gpio_pin
        self.location = location