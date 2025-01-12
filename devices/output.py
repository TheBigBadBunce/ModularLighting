from logutils import print
from dimutils import get_dim
from ioutils import setup_led, create_pwm
from constants import GPIO_PIN_MIN, GPIO_PIN_MAX
from time import sleep

class OutputDevice():
    """A single LED"""
    gpio_pin = None
    pwm = None
    location = ""
    level = 0.0
    max_level = GPIO_PIN_MAX
    min_level = GPIO_PIN_MIN

    def update_output(self):
        """Push updated value to device"""
        global_dim = get_dim()
        self.pwm.ChangeDutyCycle(self.level * global_dim * 100) # 0-100 for PWM percentage

    def set_level(self, value, silent=False):
        """Set the PWM level"""
        if not silent:
            print(f"Setting {self.location} to {value}")
        self.level = value
        self.update_output()

    def dim_level(self, end_level, length):
        """Dims the PWM level"""
        start_level = self.level
        difference = end_level - start_level

        print(f"Dimming {self.location} from {start_level} to {end_level} ({length}s)")

        for i in range (0, 100):
            self.set_level(start_level + difference * (i/100), silent=True)
            sleep(length/100)
        print(f"Dimming complete.")

    def set_max(self):
        """Set the level to maximum"""
        self.set_level(self.max_level)

    def set_min(self):
        """Set the level to minimum"""
        self.set_level(self.min_level)

    def __init__(self, gpio_pin, location, min_level = GPIO_PIN_MIN, max_level = GPIO_PIN_MAX):
        super().__init__()
        self.gpio_pin = gpio_pin
        self.location = location
        self.min_level = min_level
        self.max_level = max_level

        setup_led(self.gpio_pin)
        self.pwm = create_pwm(self.gpio_pin)
        self.pwm.start(self.level)
