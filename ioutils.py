import signal
import sys

import RPi.GPIO as GPIO # type: ignore because we develop off the pi

from logging import print_sigint_message
from constants import GPIO_PWM_FREQ

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
    GPIO.output(pin, GPIO.LOW)

def create_pwm(pin):
    """Create a PWM  object for an LED"""
    return GPIO.PWM(pin, GPIO_PWM_FREQ)

def close_GPIO():
    """Shut down all GPIO functions"""
    GPIO.cleanup()