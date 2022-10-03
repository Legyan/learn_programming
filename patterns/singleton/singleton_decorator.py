def singleton(class_):
    _instance = None

    def get_instance(*args, **kwargs):
        nonlocal _instance
        if _instance is None:
            _instance = class_(*args, **kwargs)
    return get_instance


@singleton
class Database:
    def __init__(self):
        print("Loading Database")


if __name__ == '__main__':
    db1 = Database()
    db2 = Database()
    print(db1 is db2)
