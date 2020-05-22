import time
import unittest
from unittest.mock import Mock

from timeouter.timeouter import Timeouter
from timeouter.trigger import Trigger

SHORT_WAITING_TIME = 1
LONG_WAITING_TIME = 10000


# TODO: sleeps in tests are bad - consider improving them

class TestTimeouter(unittest.TestCase):
    def setUp(self):
        self.mock_trigger = Mock(spec=Trigger)

    def test_verify_on_called_on_trigger(self):
        timeouter = Timeouter(LONG_WAITING_TIME, self.mock_trigger)

        timeouter.update()

        self.mock_trigger.turn_on.assert_called_once()
        self.mock_trigger.turn_off.assert_not_called()

    def test_trigger_then_wait_should_cancel_after_timeout(self):
        timeouter = Timeouter(SHORT_WAITING_TIME, self.mock_trigger)

        timeouter.update()

        time.sleep(SHORT_WAITING_TIME + 2)

        self.mock_trigger.turn_on.assert_called_once()
        self.mock_trigger.turn_off.assert_called_once()

    def test_multiple_triggers_should_activate_and_cancel_only_once(self):
        timeouter = Timeouter(SHORT_WAITING_TIME, self.mock_trigger)

        timeouter.update()
        timeouter.update()

        time.sleep(SHORT_WAITING_TIME + 2)

        self.mock_trigger.turn_on.assert_called_once()
        self.mock_trigger.turn_off.assert_called_once()

    def test_multiple_triggers_should_cancel_at_the_right_time(self):
        timeouter = Timeouter(5, self.mock_trigger)

        timeouter.update()
        time.sleep(3)
        timeouter.update()

        time.sleep(3)
        self.mock_trigger.turn_off.assert_not_called()
        time.sleep(3)
        self.mock_trigger.turn_off.assert_any_call()

    def test_at_startup_should_turn_on_then_off(self):
        Timeouter(SHORT_WAITING_TIME, self.mock_trigger)

        time.sleep(SHORT_WAITING_TIME + 2)

        self.mock_trigger.turn_on.assert_called_once()
        self.mock_trigger.turn_off.assert_called_once()


if __name__ == '__main__':
    unittest.main()
