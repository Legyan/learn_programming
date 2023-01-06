import time


def timer(func):
    def wrapper():
        start = time.time()
        result = func()
        timer = time.time() - start
        print(f'{func.__name__} ran for {timer}s')
        return result
    return wrapper

@timer
def test_func():
    time.sleep(1)
    print('1 sec sleep')


if __name__ == '__main__':
    test_func()