import threading

import RPi.GPIO as GPIO


class GPIOListener:
    def __init__(self, pin, verbose, timeouter):
        self._pin = pin
        self._verbose = verbose
        self._timeouter = timeouter

        self.interrupted = threading.Event()

    def start(self):
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self._pin, GPIO.IN)

            GPIO.add_event_detect(self._pin, GPIO.RISING, callback=self.motion)
            self.interrupted.wait()
        finally:
            GPIO.remove_event_detect(self._pin)
            GPIO.cleanup()
            print('Shutdown gracefully.')

    def motion(self, channel):
        if self._verbose:
            print(f'Motion detected on channel {channel}!')

        self._timeouter.update()

    def interrupt(self):
        self.interrupted.set()
