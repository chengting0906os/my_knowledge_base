import time


def timer(func):
    def wrapper(*args, **kwargs):
        now = time.time()
        result = func(*args, **kwargs)
        print(time.time() - now)
        return result

    return wrapper


@timer
def outer():
    print('1')
    return

if __name__ == "__main__":
    outer()
    outer()
    outer()