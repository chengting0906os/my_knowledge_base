# Mock Interview — Q3
#
# 實作一個 decorator @retry(n)
# 被裝飾的函式如果拋出例外，自動重試最多 n 次
# 超過 n 次還是失敗就把最後的例外拋出去

from functools import wraps
from typing import Any, Callable, TypeVar

F = TypeVar("F", bound=Callable[..., Any]) # ... 參數不限, Any 表示回傳值不限


def retry(n: int) -> Callable[[F], F]:
    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for _ in range(n):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exc = e
            raise last_exc

        return wrapper

    return decorator


# 測試用：模擬前兩次失敗，第三次成功
call_count = 0


@retry(3)
def unstable():
    global call_count
    call_count += 1
    if call_count < 3:
        raise ValueError("not ready")
    return "ok"


assert unstable() == "ok"
assert call_count == 3
print("passed")
