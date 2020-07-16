"""
在多线程中，由于子线程和主线程不同一个栈，子线程抛出的异常是不能够被
主线程捕获的。也就意味着，子线程挂了，主线程还不知道。

针对这种情况，我们需要利用对象变量，在主线程中观察变量值是否发生改变，从而得知
子线程是否存活

"""

from threading import Thread
import traceback
import sys

class demo(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.exitcode = 0
        self.exception = None
        self.exc_traceback = ''

    def run(self):
        try:
            self.main()
        except Exception as e:
            self.exitcode = 1
            self.exc_traceback = ''.join(traceback.format_exception(*sys.exc_info()))
            self.exception = e

    def main(self):
        raise Exception('这是我主动抛出的异常')



if __name__ == '__main__':
    d = demo()
    d.start()
    d.join()
    if d.exitcode == 1:
        print(d.exception)