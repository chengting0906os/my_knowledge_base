# Q1. 實作一個 decorator @timer
# 在函式執行前後計時，印出執行時間

import time
from functools import wraps
from typing import Any, Callable


def timer(func: Callable[..., Any]) -> Callable[..., Any]:

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        now = time.time()
        result = func(*args, **kwargs)
        print(time.time() - now)
        return result

    return wrapper


@timer
def slow_function():
    time.sleep(0.1)
    return "done"


if __name__ == "__main__":
    result = slow_function()
    assert result == "done"
    print("passed")
