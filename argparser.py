import argparse


class MotionArgParser:
    def __init__(self):
        parser = argparse.ArgumentParser(description='Activates motion detection')
        parser.add_argument('--pin', required=True, type=int,
                            help='the GPIO pin of the motion detector')
        parser.add_argument('--timeout', required=False, default=120, type=int,
                            help='the timeout in seconds for the screen to turn off after motion')
        parser.add_argument('-v', '--verbose', required=False, action='store_true',
                            help='activates verbose mode for motion detection')

        args = vars(parser.parse_args())

        self._pir_pin = args['pin']
        self._timeout = args['timeout']
        self._verbose = args['verbose']

    def pin(self) -> int:
        return self._pir_pin

    def timeout(self) -> int:
        return self._timeout

    def verbose(self) -> bool:
        return self._verbose
