import sys
import time
import unittest

import pexpect
from readchar import key

from tests.acceptance.utils import send_key


@unittest.skipIf(sys.platform.startswith("win"), "Without Windows")
class ShortcutsTest(unittest.TestCase):
    EOF_STRING = ":.*"

    def send_key(self, key_to_press: str, times: int = 1):
        send_key(self.sut, self.EOF_STRING, key_to_press, times=times)

    def setUp(self):
        self.sut = pexpect.spawn("python examples/shortcuts.py")

    def test_shortcuts(self):
        # username
        self.send_key("foo")
        self.sut.expect("foo")
        self.sut.send(key.ENTER)

        # password
        self.send_key("secret")
        self.sut.expect(r"\*{6}", timeout=1)
        self.sut.send(key.ENTER)

        # checkbox
        self.sut.expect("frontend.*", timeout=1)
        self.sut.send(key.ENTER)
        time.sleep(0.5)

        # list
        self.sut.expect("private.*", timeout=1)
        self.sut.send(key.ENTER)

        # confirm
        self.send_key("y")
        self.sut.expect("True", timeout=1)
