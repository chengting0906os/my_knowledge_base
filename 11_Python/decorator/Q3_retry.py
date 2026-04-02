# Q3. 實作一個帶參數的 decorator @retry(n)
# 函式拋出例外時自動重試，最多重試 n 次
# 超過 n 次還是失敗就把最後的例外拋出去


from functools import wraps
from typing import Any, Callable


def retry(n=3) -> Callable[..., Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for _ in range(n):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    exc = e

            raise exc

        return wrapper

    return decorator


call_count = 0


@retry(3)
def unstable():
    global call_count
    call_count += 1
    if call_count < 3:
        raise ValueError("not ready")
    return "ok"


if __name__ == "__main__":
    assert unstable() == "ok"
    assert call_count == 3
    print("passed")
