"""
__new__方法
"""

class Sigleton(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Sigleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)

        return cls._instance

a = Sigleton()
b = Sigleton()
print(id(a), id(b))

"""装饰器版本"""
def singleton(cls):
    instance = {}
    def getInstance(*args, **kws):
        if cls not in instance:
            instance[cls] = cls(*args, **kw)
        return instance[cls]
    return getInstance

@singleton
def test1():
    pass

@singleton
def test2():
    pass

a =test1()
b = test2()
print(id(a), id(b))

