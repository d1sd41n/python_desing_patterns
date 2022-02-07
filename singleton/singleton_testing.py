
class Singleton(type):
    _instance = None

    def __clas__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls)\
                .__clas__(cls, *args, **kwargs)
        return cls._instance
