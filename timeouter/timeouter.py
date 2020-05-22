import time
from threading import RLock, Event, Thread

from timeouter.trigger import Trigger


class Timeouter(Thread):
    def __init__(self, timeout: int, trigger: Trigger):
        super().__init__()
        self.timeout = timeout
        self.trigger = trigger
        self.event_active = Event()
        self.interrupted = Event()
        self.lock = RLock()
        self.expiry = self._updated_expiry()

        # start thread
        self.start()

        # start with activity, and allow expiry (and turning off) to be triggered
        self.update()

    def update(self):
        self.expiry = self._updated_expiry()

        self.lock.acquire()
        try:
            if not self.event_active.is_set():
                self.trigger.turn_on()
                self.event_active.set()
        finally:
            self.lock.release()

    def run(self) -> None:
        while not self.interrupted.is_set():
            # block until an activity occurs
            self.event_active.wait()

            self.interrupted.wait(
                max(self.expiry - time.time(), 0)
            )

            self.lock.acquire()
            try:
                if time.time() > self.expiry:
                    self.trigger.turn_off()
                    self.event_active.clear()
            finally:
                self.lock.release()

    def interrupt(self):
        self.interrupted.set()
        self.event_active.set()

    def _updated_expiry(self):
        return time.time() + self.timeout
