import sys
import unittest

import pexpect
from readchar import key

from tests.acceptance.utils import send_key


@unittest.skipIf(sys.platform.startswith("win"), "Without Windows")
class TextTest(unittest.TestCase):
    EOF_STRING = ":.*"

    def send_key(self, key_to_press: str, times: int = 1):
        send_key(self.sut, self.EOF_STRING, key_to_press, times=times)

    def setUp(self):
        self.sut = pexpect.spawn("python examples/text.py")

    def set_name(self, name="foo"):
        self.sut.expect("What's", timeout=1)
        self.sut.sendline(name)

    def set_surname(self, surname="bar"):
        self.sut.expect("What's", timeout=1)
        self.sut.sendline(surname)

    def set_phone(self, phone="123456789"):
        self.sut.expect("What's", timeout=1)
        self.sut.sendline(phone)

    def test_default_input(self):
        self.send_key("foo")
        self.sut.expect("foo.*")
        self.sut.send(key.ENTER)

        self.send_key("bar")
        self.sut.expect("bar.*")
        self.sut.send(key.ENTER)

        self.send_key("123456789")
        self.sut.expect("123456789.*")
        self.sut.send(key.ENTER)

        self.sut.expect("{'name': 'foo', 'phone': '123456789', 'surname': 'bar'}.*", timeout=1)

    def test_invalid_phone(self):
        self.send_key("foo")
        self.sut.expect("foo.*")
        self.sut.send(key.ENTER)

        self.send_key("bar")
        self.sut.expect("bar.*")
        self.sut.send(key.ENTER)

        self.send_key("abcde")
        self.sut.expect("abcde.*")
        self.sut.send(key.ENTER)

        self.sut.expect("I don't like your phone number!", timeout=1)
        self.send_key(key.BACKSPACE, times=5)

        self.send_key("12345")
        self.sut.expect("12345.*")
        self.sut.send(key.ENTER)

        self.sut.expect("{'name': 'foo', 'phone': '12345', 'surname': 'bar'}.*", timeout=1)


@unittest.skipIf(sys.platform.startswith("win"), "Without Windows")
class TextAutocompleteTest(unittest.TestCase):
    def setUp(self):
        self.sut = pexpect.spawn("python examples/text_autocomplete.py")

    def test_autocomplete(self):
        self.sut.expect(": .*", timeout=1)
        self.sut.send("random")
        self.sut.expect(": random.*", timeout=1)
        self.sut.send(key.TAB)
        self.sut.expect(": inquirer3.*", timeout=1)
        self.sut.send(key.ENTER)
        self.sut.expect("{'name': 'inquirer3'}", timeout=1)
