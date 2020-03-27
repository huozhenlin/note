class Subject(object):

    def __init__(self):
        self._observer = []

    def add(self, observer):
        if observer not in self._observer:
            self._observer.append(observer)

    def remover(self, observer):
        if observer in self._observer:
            self._observer.remove(observer)

    def notify(self):
        for observer in self._observer:
            observer.update(self)


class Data(Subject):

    def __init__(self, name):
        Subject.__init__(self)
        self.name = name
        self._data = ''

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.notify()


class Girl:

    def update(self, observer):
        print('Girl, data {} change to {}'.format(observer.name, observer._data))


class Boy:
    def update(self, observer):
        print('Boy, data {} change to {}'.format(observer.name, observer._data))


data = Data('data1')
girl = Girl()
boy = Boy()
data.add(girl)
data.add(boy)
data.data = 'data2'
data.remover(girl)