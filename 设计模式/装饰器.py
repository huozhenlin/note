from functools import wraps
# def makebold(fn):
#     @wraps(fn)
#     def wrapped(*args, **kwargs):
#         return "<b>" + fn(*args, **kwargs) + "</b>"
#     return wrapped
#
# def makeitalic(fn):
#     @wraps(fn)
#     def wrapped(*args, **kwargs):
#         return "<i>" + fn(*args, **kwargs) + "</i>"
#     return wrapped

# @makebold
# @makeitalic
# def hello():
#     return "hello world"

from datetime import datetime

def makelogs(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        print('{}调用了方法:{}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), fn.__name__))
    return wrapped


@makelogs
def test():
    pass
test()