import RPi.GPIO as GPIO # type: ignore because we develop off the pi
from datetime import time

GPIO_PIN_MAX = GPIO.HIGH
GPIO_PIN_MIN = GPIO.LOW
GPIO_PWM_FREQ = 100

LOGFILE_REALTIME = "realtime.log"
LOGFILE_SIMULATE = "simulate.log"
LOGFILE_FULL = "full.log"

DAILY_RESET_TIME = time(4,00)

SIMULATION_TICKS_PER_SECOND = 60
PIR_DIM_DROPOFF_PER_TICK = 0.025
DIM_MAX = 1.0
DIM_MIN = 0.0