import subprocess

from timeouter.trigger import Trigger


class ScreenTrigger(Trigger):
    def turn_on(self):
        subprocess.call(['tvservice', '-p'])
        subprocess.call(['sudo', 'chvt', '6'])
        subprocess.call(['sudo', 'chvt', '7'])

    def turn_off(self):
        subprocess.call(['tvservice', '-o'])
