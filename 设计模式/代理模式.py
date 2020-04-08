class Proxy():

    def __init__(self, subject):
        self.__subject = subject

    def __getattr__(self, item):
        return getattr(self.__subject, item)


class RGB:
    def __init__(self, red, green, blue):
        self.__red = red
        self.__greeen = green
        self.__blue = blue

    def RED(self):
        return self.__red

    def GREEN(self):
        return self.__greeen

    def BLUE(self):
        return self.__blue

class NOBlueProxy(Proxy):

    def BLUE(self):
        return 0


rgb = RGB(100, 192, 240)
print(rgb.RED())
proxy = Proxy(rgb)
print(proxy.GREEN())
noblue = NOBlueProxy(rgb)
print(noblue.BLUE())
