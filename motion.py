#!/usr/bin/python3
import time

import RPi.GPIO as GPIO

from screen import ScreenTrigger
from timeouter.timeouter import Timeouter

# Configuration

PIR_PIN = 18
TIMEOUT = 300

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

screen = ScreenTrigger()
timeouter = Timeouter(TIMEOUT, screen)


def motion(channel):
    timeouter.update()


try:
    GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=motion)
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    GPIO.cleanup()
