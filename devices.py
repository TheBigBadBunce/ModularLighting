from logging import print
from dimutils import get_dim
from ioutils import get_input, setup_led, setup_input, create_pwm

class OutputDevice():
    """A single LED"""
    gpio_pin = None
    pwm = None
    location = ""
    level = 0

    def update_output(self):
        global_dim = get_dim()
        self.pwm.ChangeDutyCycle(self.level * global_dim * 100) # 0-100 for PWM percentage

    def set_level(self, value):
        """Set the power(?) on the device's GPIO pin"""
        print(f"Setting {self.location} to {value}")
        self.level = value
        self.update_output()

    def __init__(self, gpio_pin, location):
        super().__init__()
        self.gpio_pin = gpio_pin
        self.location = location

        setup_led(self.gpio_pin)
        self.pwm = create_pwm(self.gpio_pin)
        self.pwm.start(self.level)

class InputDevice():
    """A true/false input e.g PIR sensor"""
    gpio_pin = None

    def get_level(self):
        return get_input(self.gpio_pin)

    def __init__(self, gpio_pin):
        super().__init__()
        self.gpio_pin = gpio_pin

        setup_input(self.gpio_pin)

