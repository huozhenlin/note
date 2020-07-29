class Person():
    def speak(self):
        pass

    def paly(self):
        pass


class Boy(Person):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print('my name is '+self.name)

    def paly(self):
        print("{}_{}".format(self.name, 'playing'))


class HookeMethodClass():

    def __init__(self):
        self.hook_method = []

    def register_metod_hook(self, method):
        self.hook_method.append(method)

    def unregister_metod_hook(self, method):
        self.hook_method.remove(method)

    def play(self):
        print("哈哈")


    def run(self):
        if not self.hook_method:
            print("未接收到需要hook的方法")
        else:
            for method in self.hook_method:
                method()



if __name__ == '__main__':

    boy = Boy('A')
    hook = HookeMethodClass()
    hook.register_metod_hook(boy.speak)
    hook.register_metod_hook(boy.paly)
    hook.run()
    hook.unregister_metod_hook(boy.paly)
    hook.run()

