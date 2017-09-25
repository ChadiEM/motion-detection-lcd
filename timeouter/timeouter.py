import sched
import threading
import time

from timeouter.trigger import Trigger


class Timeouter:
    def __init__(self, timeout: int, trigger: Trigger):
        self.timeout = timeout
        self.trigger = trigger
        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.event = None

    def update(self):
        if self.event is not None:
            try:
                self.scheduler.cancel(self.event)
            except ValueError:
                pass
        else:
            self.__on()

        self.event = self.scheduler.enter(self.timeout, 1, self.__off, ())
        self.__run_in_thread()

    def __on(self):
        self.trigger.turn_on()

    def __off(self):
        self.event = None
        self.trigger.turn_off()

    def __run_in_thread(self):
        t = threading.Thread(target=self.scheduler.run)
        t.setDaemon(True)
        t.start()
