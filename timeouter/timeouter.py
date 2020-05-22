import time
from threading import RLock, Event, Thread

from timeouter.trigger import Trigger


class Timeouter(Thread):
    def __init__(self, timeout: int, trigger: Trigger):
        super().__init__(daemon=True)
        self.timeout = timeout
        self.trigger = trigger
        self.event_active = Event()
        self.lock = RLock()
        self.expiry = self._updated_expiry()

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
        while True:
            # block until an activity occurs
            self.event_active.wait()

            time.sleep(max(self.expiry - time.time(), 0))

            self.lock.acquire()
            try:
                if time.time() > self.expiry:
                    self.trigger.turn_off()
                    self.event_active.clear()
            finally:
                self.lock.release()

    def _updated_expiry(self):
        return time.time() + self.timeout
