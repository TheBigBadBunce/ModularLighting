import RPi.GPIO as GPIO # type: ignore because we develop off the pi

GPIO_PIN_MAX = GPIO.HIGH
GPIO_PIN_MIN = GPIO.LOW

LOGFILE_REALTIME = "realtime.log"
LOGFILE_OFFSET = "offset.log"
LOGFILE_SIMULATE = "simulate.log"
