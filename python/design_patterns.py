'''
Creational Patterns
'''
# SINGLETON
class MetaSingleton():
    _instances = {}

    # this works by making the class and instance of the metasingleton
    # class, when the class is created it calls __call__
    def __call__(cls, *args, **kwargs):
        if cls not in _instances:
            #we want to call cls


def factory_method():
    pass

# strategy

# observer

# builder 

# adapter

# state