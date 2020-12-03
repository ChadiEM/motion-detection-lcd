import threading

from gpiozero import MotionSensor


class GPIOListener:
    def __init__(self, pin, verbose, timeouter):
        self._pin = pin
        self._verbose = verbose
        self._timeouter = timeouter

        self.interrupted = threading.Event()

    def start(self):
        pir = MotionSensor(self._pin)
        try:
            pir.when_motion = self.motion
            self.interrupted.wait()
        finally:
            pir.close()
            print('Shutdown gracefully.')

    def motion(self, channel):
        if self._verbose:
            print(f'Motion detected on {channel.pin}!')

        self._timeouter.update()

    def interrupt(self):
        self.interrupted.set()
