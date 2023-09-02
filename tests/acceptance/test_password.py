import sys
import unittest

import pexpect
from readchar import key

from tests.acceptance.utils import send_key


@unittest.skipIf(sys.platform.startswith("win"), "Without Windows")
class PasswordTest(unittest.TestCase):
    EOF_STRING = ".*What's.*"
    INPUT = "abcde"

    def send_key(self, key_to_press: str, times: int = 1):
        send_key(self.sut, self.EOF_STRING, key_to_press, times=times)

    def setUp(self):
        self.sut = pexpect.spawn("python examples/password.py")

    def test_default_input(self):
        self.send_key(self.INPUT)
        self.sut.expect(rf"\*{{{len(self.INPUT)}}}", timeout=1)
        self.sut.send(key.ENTER)
        self.sut.expect("{'password': 'abcde'}.*", timeout=1)

    def test_backspace(self):
        self.send_key(self.INPUT)
        self.sut.expect(rf"\*{{{len(self.INPUT)}}}", timeout=1)
        self.sut.send(key.BACKSPACE)
        self.sut.expect(rf"\*{{{len(self.INPUT) - 1}}}", timeout=1)
        self.sut.send(key.ENTER)
        self.sut.expect("{'password': 'abcd'}.*", timeout=1)

    def test_backspace_limit(self):
        self.send_key("a")
        self.send_key(key.BACKSPACE)
        self.send_key(key.BACKSPACE)
        self.send_key("b")
        self.send_key(key.ENTER)
        self.sut.expect("{'password': 'b'}.*", timeout=1)
