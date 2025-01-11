from ioutils import get_input, setup_input

class InputDevice():
    """A true/false input e.g PIR sensor"""
    gpio_pin = None

    def get_level(self):
        return get_input(self.gpio_pin)

    def __init__(self, gpio_pin):
        super().__init__()
        self.gpio_pin = gpio_pin

        setup_input(self.gpio_pin)

