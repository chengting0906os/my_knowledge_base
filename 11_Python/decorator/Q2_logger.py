# Q2. 實作一個 decorator @logger
# 每次呼叫函式時，印出函式名稱、傳入的參數、回傳值

from functools import wraps
from typing import Any, Callable


def logger(func: Callable[..., Any]) -> Callable[..., Any]:

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result

    return wrapper


@logger
def add(x, y):
    return x + y


if __name__ == "__main__":
    result = add(3, 4)
    assert result == 7
    # 預期印出類似：
    # calling add(3, 4)
    # add returned 7
    print("passed")
