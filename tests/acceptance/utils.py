import time
from typing import Union


def send_key(child, expect_for: str, key_to_press: str, times: int = 1, sleep_time: Union[float, int] = 0):
    for _ in range(times):
        child.expect(expect_for, timeout=2)
        child.send(key_to_press)
        if sleep_time:
            time.sleep(sleep_time)
