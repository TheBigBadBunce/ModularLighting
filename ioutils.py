import signal
import sys

import RPi.GPIO as GPIO # type: ignore because we develop off the pi

from logging import print_sigint_message

def initialise_GPIO():
    """Prime GPIO for IO and set sigint handler"""
    GPIO.setmode(GPIO.BCM)
    
    def signal_handler(sig, frame):
        print_sigint_message()
        close_GPIO()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

def setup_led(pin):
    """Register a single LED with GPIO"""
    GPIO.setup(pin, GPIO.OUT)

def set_GPIO_pin(pin, value):
    """Set the output on an LED"""
    GPIO.output(pin, value)

def close_GPIO():
    """Shut down all GPIO functions"""
    GPIO.cleanup()