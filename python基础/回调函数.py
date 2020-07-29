def test(callback):
    print('方法体已经执行完毕，下面执行回调')
    callback()


def callback_1():
    print('程序结束')


test(callback_1)