import sys
import unittest
from typing import Union

import pexpect
from readchar import key

from tests.acceptance.utils import send_key

expected_result = (
    r"{'correct': True,\r\n "
    r"'organization': '',\r\n "
    r"'password': 'edcba',\r\n "
    r"'repo': 'default',\r\n "
    r"'topics': \['common'\],\r\n "
    r"'user': 'abcde'}\r\n"
)


@unittest.skipIf(sys.platform.startswith("win"), "Without Windows")
class PreAnswersTest(unittest.TestCase):
    EOF_STRING = ":.*"

    def send_key(self, key_to_press: str, times: int = 1, sleep_time: Union[float, int] = 0.2):
        send_key(self.sut, self.EOF_STRING, key_to_press, times=times, sleep_time=sleep_time)

    def setUp(self):
        self.sut = pexpect.spawn("python examples/pre_answers.py")

    def test_minimal_input(self):
        # user
        self.send_key("abcde")
        self.sut.expect("abcde", timeout=1)
        self.sut.send(key.ENTER)

        # password
        self.send_key("edcba")
        self.sut.expect(r"\*{5}", timeout=1)
        self.sut.send(key.ENTER)

        # repo
        self.send_key(key.ENTER)

        # topics
        self.send_key(key.SPACE)
        self.send_key(key.ENTER)

        # organization
        self.send_key(key.ENTER)

        # correct
        self.send_key("y")

        # again
        self.send_key(key.ENTER, times=6)

        self.sut.expect([expected_result, pexpect.EOF], timeout=1)
