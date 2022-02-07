def singleton(class_):
    instances = {}

    def get_instances(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instances

@singleton
class Database:
    def __init__(self) -> None:
        print("loadinf db")