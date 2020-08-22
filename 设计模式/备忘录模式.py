import copy

def Memento(obj, deep=False):

    state = (copy.copy if deep else copy.deepcopy)(obj.__dict__)

    def Restore():
        obj.__dict__ = state

    return Restore

class Transaction:

    deep = False

    def __init__(self, *targets):
        self.targets = targets
        self.Commit()

    def Commit(self):
        self.states = [Memento(target, self.deep) for target in self.targets]

    def Rollback(self):
        for state in self.states:
            state()

def transactional(method):

    def wrappedMethod(self, *args, **kwargs):
        state = Memento(self)
        try:
            return method(self, *args, **kwargs)
        except Exception as e:
            print(e.args)
            state()
            raise
    return wrappedMethod

class NumObj(object):

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return '<%s: %r>'%(self.__class__.__name__, self.value)

    def Increment(self):
        self.value += 1

    @transactional
    def DoStuff(self):
        # 赋值成字符串，再自增长肯定会报错的
        self.value = '1111'
        self.Increment()

if __name__ == '__main__':
    n = NumObj(-1)
    print(n)
    t = Transaction(n)
    try:
        for i in range(3):
            n.Increment()
            print(n)
        t.Commit()
        print('-- commited')
        for i in range(3):
            n.Increment()
            print(n)
        n.value += 'x'  # will fail
        print(n)
    except:
        # 回滚只会回顾到上一次comit成功的2 而不是-1
        t.Rollback()
        print('-- rolled back')
    print(n)
    print('-- now doing stuff ...')
    try:
        n.DoStuff()
    except:
        print('-> doing stuff failed!')
        import traceback

        traceback.print_exc(0)
        pass
    # 第二次的异常回滚n还是2, 整个过程都是修改NumObj的实例对象
    print(n)