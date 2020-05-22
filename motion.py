#!/usr/bin/env python3
import signal

from argparser import MotionArgParser
from gpio_listener import GPIOListener
from screen import ScreenTrigger
from timeouter.timeouter import Timeouter

if __name__ == '__main__':
    parser = MotionArgParser()

    print(f'Starting motion detection:'
          f' pin={str(parser.pin())},'
          f' timeout={str(parser.timeout())}s,'
          f' verbose={str(parser.verbose())}')

    screen = ScreenTrigger()
    timeouter = Timeouter(parser.timeout(), screen)

    gpio_listener = GPIOListener(parser.pin(), parser.verbose(), timeouter)


    def interrupt(signum, frame):
        print(f'Caught signal {signum}')
        gpio_listener.interrupt()
        timeouter.interrupt()


    signal.signal(signal.SIGINT, interrupt)
    signal.signal(signal.SIGTERM, interrupt)

    gpio_listener.start()
