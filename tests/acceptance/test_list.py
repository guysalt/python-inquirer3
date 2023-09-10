import sys
import unittest
from typing import Union

import pexpect
from readchar import key

from tests.acceptance.utils import send_key


@unittest.skipIf(sys.platform.startswith("win"), "Without Windows")
class ListTest(unittest.TestCase):
    EOF_STRING = "Micro.*"

    def send_key(self, key_to_press: str, times: int = 1, sleep_time: Union[float, int] = 0):
        send_key(self.sut, self.EOF_STRING, key_to_press, times=times, sleep_time=sleep_time)

    def setUp(self):
        self.sut = pexpect.spawn("python examples/list.py")

    def test_default_input(self):
        self.send_key(key.ENTER)
        self.sut.expect("{'size': 'Jumbo'}.*", timeout=1)

    def test_change_selection(self):
        self.send_key(key.DOWN)
        self.send_key(key.ENTER)
        self.sut.expect("{'size': 'Large'}.*", timeout=1)

    def test_out_of_bounds_up(self):
        self.send_key(key.UP)
        self.send_key(key.ENTER)
        self.sut.expect("{'size': 'Jumbo'}.*", timeout=1)

    def test_out_of_bounds_down(self):
        self.send_key(key.DOWN, times=10, sleep_time=0.1)
        self.send_key(key.ENTER)
        self.sut.expect("{'size': 'Micro'}.*", timeout=1)


@unittest.skipIf(sys.platform.startswith("win"), "Without Windows")
class ListCarouselTest(unittest.TestCase):
    EOF_STRING = "Standard.*"

    def send_key(self, key_to_press: str, times: int = 1, sleep_time: Union[float, int] = 0.2):
        send_key(self.sut, self.EOF_STRING, key_to_press, times=times, sleep_time=sleep_time)

    def setUp(self):
        self.sut = pexpect.spawn("python examples/list_carousel.py")

    def test_out_of_bounds_up(self):
        self.send_key(key.UP)
        self.send_key(key.ENTER)
        self.sut.expect("{'size': 'Standard'}.*", timeout=1)

    def test_out_of_bounds_down(self):
        self.send_key(key.DOWN, times=3)
        self.send_key(key.ENTER)
        self.sut.expect("{'size': 'Jumbo'}.*", timeout=1)


@unittest.skipIf(sys.platform.startswith("win"), "Without Windows")
class CheckOtherTest(unittest.TestCase):
    EOF_STRING = "Other.*"

    # Special sleep for this case
    def send_key(self, key_to_press: str, times: int = 1, sleep_time: Union[float, int] = 0.2):
        send_key(self.sut, self.EOF_STRING, key_to_press, times=times, sleep_time=sleep_time)

    def setUp(self):
        self.sut = pexpect.spawn("python examples/list_other.py")

    def test_other_input(self):
        self.send_key(key.UP)
        self.send_key(key.ENTER)
        self.sut.expect(":.*", timeout=1)
        self.sut.send("Hello world")
        self.sut.expect("Hello world.*", timeout=1)
        self.sut.send(key.ENTER)
        self.sut.expect("{'size': 'Hello world'}.*", timeout=1)

    def test_other_blank_input(self):
        self.send_key(key.UP)
        self.send_key(key.ENTER)
        self.sut.expect(":.*", timeout=1)
        self.sut.send(key.ENTER)  # blank input
        self.sut.expect(r"\+ Other.*", timeout=1)
        self.sut.send(key.ENTER)
        self.sut.expect(":.*", timeout=1)
        self.sut.send("Hello world")
        self.sut.expect("Hello world.*", timeout=1)
        self.sut.send(key.ENTER)
        self.sut.expect("{'size': 'Hello world'}.*", timeout=1)

    def test_other_select_choice(self):
        self.send_key(key.ENTER)
        self.sut.expect("{'size': 'Jumbo'}.*", timeout=1)


@unittest.skipIf(sys.platform.startswith("win"), "Without Windows")
class ListTaggedTest(unittest.TestCase):
    def setUp(self):
        self.sut = pexpect.spawn("python examples/list_tagged.py")
        self.sut.expect("Micro.*", timeout=1)

    def test_default_input(self):
        self.sut.send(key.ENTER)
        self.sut.expect("{'size': 'xxl'}.*", timeout=1)
