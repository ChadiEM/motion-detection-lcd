import os
import subprocess

from timeouter.trigger import Trigger


class ScreenTrigger(Trigger):
    def turn_on(self):
        print('Turning screen on.')

        env = dict(os.environ, XAUTHORITY="~/.Xauthority", DISPLAY=':0')

        subprocess.call('xset dpms force on', shell=True, env=env)
        subprocess.call('xset -dpms', shell=True, env=env)
        subprocess.call('xset s off', shell=True, env=env)

    def turn_off(self):
        print('Turning screen off.')

        env = dict(os.environ, XAUTHORITY="~/.Xauthority", DISPLAY=':0')

        subprocess.call('xset dpms force off', shell=True, env=env)
        subprocess.call('xset s off', shell=True, env=env)
