class Device():
    gpio_pin = None
    location = ""

    def set_gpio_pin(self, value):
        # TODO
        print(f"Setting {self.location} to {value}")
        pass

    def __init__(self, gpio_pin, location):
        super().__init__()
        self.gpio_pin = gpio_pin
        self.location = location   