import sys
import unittest
from re import escape

import pexpect
from readchar import key

from inquirer3.themes import Default as Theme
from tests.acceptance.utils import send_key


@unittest.skipIf(sys.platform.startswith("win"), "Without Windows")
class CheckTest(unittest.TestCase):
    EOF_STRING = "History.*"

    def send_key(self, key_to_press: str, times: int = 1):
        send_key(self.sut, self.EOF_STRING, key_to_press, times=times)

    def setUp(self):
        self.sut = pexpect.spawn("python examples/checkbox.py")

    def test_default_input(self):
        self.send_key(key.ENTER)
        self.sut.expect(r"{'interests': \['Computers', 'Books'\]}.*", timeout=1)  # noqa

    def test_select_the_third(self):
        self.send_key(key.DOWN, times=2)
        self.send_key(key.SPACE)
        self.send_key(key.ENTER)
        self.sut.expect(r"{'interests': \['Computers', 'Books', 'Science'\]}.*", timeout=1)  # noqa

    def test_select_one_more(self):
        self.send_key(key.DOWN, times=2)
        self.send_key(key.SPACE)
        self.send_key(key.DOWN)
        self.send_key(key.SPACE)
        self.send_key(key.ENTER)
        self.sut.expect(r"{'interests': \['Computers', 'Books', 'Science', 'Nature'\]}.*", timeout=1)  # noqa

    def test_unselect(self):
        self.send_key(key.SPACE)
        self.send_key(key.SPACE)
        self.send_key(key.ENTER)
        self.sut.expect(r"{'interests': \['Books', 'Computers'\]}.*", timeout=1)  # noqa

    def test_select_with_arrows(self):
        self.send_key(key.DOWN, times=2)
        self.send_key(key.RIGHT)
        self.send_key(key.ENTER)
        self.sut.expect(r"{'interests': \['Computers', 'Books', 'Science'\]}.*", timeout=1)  # noqa

    def test_unselect_with_arrows(self):
        self.send_key(key.DOWN)
        self.send_key(key.LEFT)
        self.send_key(key.ENTER)
        self.sut.expect(r"{'interests': \['Computers'\]}.*", timeout=1)  # noqa

    def test_select_last(self):
        self.send_key(key.DOWN, times=10)
        self.send_key(key.SPACE)
        self.send_key(key.ENTER)
        self.sut.expect(r"{'interests': \['Computers', 'Books', 'History'\]}.*", timeout=1)  # noqa

    def test_select_all_with_ctrl_a(self):
        self.send_key(key.CTRL_A)
        self.send_key(key.ENTER)
        self.sut.expect(
            r"{'interests': \['Computers', 'Books', 'Science', 'Nature', 'Fantasy', 'History'\]}.*", timeout=1
        )  # noqa

    def test_reset_with_ctrl_r(self):
        self.send_key(key.CTRL_R)
        self.send_key(key.ENTER)
        self.sut.expect(r"{'interests': \[\]}.*", timeout=1)  # noqa

    def test_default_invert_selection_with_ctrl_i(self):
        self.send_key(key.CTRL_I)
        self.send_key(key.ENTER)
        self.sut.expect(r"{'interests': \['Science', 'Nature', 'Fantasy', 'History'\]}.*", timeout=1)  # noqa


@unittest.skipIf(sys.platform.startswith("win"), "Without Windows")
class CheckCarouselTest(unittest.TestCase):
    EOF_STRING = "History.*"

    def send_key(self, key_to_press: str, times: int = 1):
        send_key(self.sut, self.EOF_STRING, key_to_press, times=times)

    def setUp(self):
        self.sut = pexpect.spawn("python examples/checkbox_carousel.py")

    def test_out_of_bounds_up(self):
        self.send_key(key.UP)
        self.send_key(key.SPACE)
        self.send_key(key.ENTER)
        self.sut.expect(r"{'interests': \['Computers', 'Books', 'History'\]}.*", timeout=1)  # noqa

    def test_out_of_bounds_down(self):
        self.send_key(key.DOWN, times=6)
        self.send_key(key.SPACE)
        self.send_key(key.ENTER)
        self.sut.expect(r"{'interests': \['Books'\]}.*", timeout=1)  # noqa


@unittest.skipIf(sys.platform.startswith("win"), "Without Windows")
class CheckOtherTest(unittest.TestCase):
    EOF_STRING = r"\+ Other.*"

    def send_key(self, key_to_press: str, times: int = 1):
        send_key(self.sut, self.EOF_STRING, key_to_press, times=times)

    def setUp(self):
        self.theme = Theme()
        self.sut = pexpect.spawn("python examples/checkbox_other.py")

    def test_other_input(self):
        self.send_key(key.UP)
        self.send_key(key.SPACE)
        self.sut.expect(":.*", timeout=1)
        self.sut.send("Hello world")
        self.sut.expect("Hello world.*", timeout=1)
        self.sut.send(key.ENTER)
        self.sut.expect(rf"> {escape(self.theme.Checkbox.selected_icon)} Hello world[\s\S]*\+ Other.*", timeout=3)
        self.sut.send(key.ENTER)
        self.sut.expect(r"{'interests': \['Computers', 'Books', 'Hello world'\]}", timeout=1)  # noqa

    def test_other_blank_input(self):
        self.send_key(key.UP)
        self.send_key(key.SPACE)
        self.sut.expect(":.*", timeout=1)
        self.sut.send(key.ENTER)  # blank input
        self.send_key(key.ENTER)
        self.sut.expect(r"{'interests': \['Computers', 'Books'\]}", timeout=1)  # noqa

    def test_other_select_choice(self):
        self.send_key(key.SPACE)
        self.send_key(key.ENTER)
        self.sut.expect(r"{'interests': \['Books'\]}", timeout=1)  # noqa


@unittest.skipIf(sys.platform.startswith("win"), "Without Windows")
class CheckWithTaggedValuesTest(unittest.TestCase):
    def setUp(self):
        self.sut = pexpect.spawn("python examples/checkbox_tagged.py")

    def test_default_selection(self):
        self.sut.expect("History.*", timeout=1)
        self.sut.send(key.ENTER)
        self.sut.expect(r"{'interests': \['c', 'b'\]}", timeout=1)


@unittest.skipIf(sys.platform.startswith("win"), "Without Windows")
class CheckLockedTest(unittest.TestCase):
    EOF_STRING = "DevOps.*"

    def send_key(self, key_to_press: str, times: int = 1):
        send_key(self.sut, self.EOF_STRING, key_to_press, times=times)

    def setUp(self):
        self.sut = pexpect.spawn("python examples/checkbox_locked.py")

    def test_default_selection(self):
        self.send_key(key.ENTER)
        self.sut.expect(r"{'courses': \['Programming fundamentals'\]}", timeout=1)

    def test_locked_option_space(self):
        self.send_key(key.SPACE)
        self.send_key(key.ENTER)
        self.sut.expect(r"{'courses': \['Programming fundamentals'\]}", timeout=1)

    def test_locked_option_left_key(self):
        self.send_key(key.LEFT)
        self.send_key(key.ENTER)
        self.sut.expect(r"{'courses': \['Programming fundamentals'\]}", timeout=1)

    def test_locked_with_another_option(self):
        self.send_key(key.DOWN, times=2)
        self.send_key(key.SPACE)
        self.send_key(key.ENTER)
        self.sut.expect(r"{'courses': \['Programming fundamentals', 'Data science'\]}", timeout=1)
