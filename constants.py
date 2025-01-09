import RPi.GPIO as GPIO # type: ignore because we develop off the pi

GPIO_PIN_MAX = GPIO.HIGH
GPIO_PIN_MIN = GPIO.LOW
GPIO_PWM_FREQ = 100

LOGFILE_REALTIME = "realtime.log"
LOGFILE_OFFSET = "offset.log"
LOGFILE_SIMULATE = "simulate.log"

SIMULATION_TICKS_PER_SECOND = 60
DIM_DROPOFF_PER_TICK = 5