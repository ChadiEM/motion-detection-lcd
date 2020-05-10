#!/usr/bin/env python3
import argparse
import time

import RPi.GPIO as GPIO

from screen import ScreenTrigger
from timeouter.timeouter import Timeouter

parser = argparse.ArgumentParser(description='Activates motion detection')
parser.add_argument('--pin', required=True, type=int,
                    help='the GPIO pin of the motion detector')
parser.add_argument('--timeout', required=False, default=120, type=int,
                    help='the timeout in seconds for the screen to turn off after motion')
parser.add_argument('-v', '--verbose', required=False, action='store_true',
                    help='activates verbose mode for motion detection')

args = vars(parser.parse_args())

pir_pin = args['pin']
timeout = args['timeout']
verbose = args['verbose']

GPIO.setmode(GPIO.BCM)
GPIO.setup(pir_pin, GPIO.IN)

screen = ScreenTrigger()
timeouter = Timeouter(timeout, screen)


def motion(channel):
    if verbose:
        print('Motion detected')

    timeouter.update()


print('Starting motion detection: pin=' + str(pir_pin) + ', timeout=' + str(timeout) + ', verbose=' + str(verbose))

try:
    GPIO.add_event_detect(pir_pin, GPIO.RISING, callback=motion)
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    GPIO.cleanup()
