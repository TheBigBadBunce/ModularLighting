from logging import print
from ioutils import setup_led, create_pwm

class Device():
    """A single LED"""
    gpio_pin = None
    pwm = None
    location = ""

    def set_gpio_pin(self, value):
        """Set the power(?) on the device's GPIO pin"""
        print(f"Setting {self.location} to {value}")
        self.pwm.ChangeDutyCycle(value * 100) # *100 bc CDC is a percentage
        pass

    def setup(self):
        """Initialise the device"""
        setup_led(self.gpio_pin)

    def __init__(self, gpio_pin, location):
        super().__init__()
        self.gpio_pin = gpio_pin
        self.pwm = create_pwm(gpio_pin)
        self.location = location