# 参考链接  https://www.cnblogs.com/linshuhui/p/9580620.html

# 官方源码
```python
class Foo:
    def __init__(self,name,count):
        self.name = name
        self.count = count
    def __hash__(self):
        print("%s调用了哈希方法"%self.name)
        return hash(id(self))
    def __eq__(self, other):
        print("%s调用了eq方法")
        if self.__dict__ == other.__dict__:
            return True
        else:return False
f1 = Foo('f1',1)
f2 = Foo('f2',2)
f3 = Foo('f3',3)
ls = [f1,f2,f3]
print(set(ls))

```

# 前言  
set 是python 存储无重复，无序的列表。参考源码，我们得知，
它的去重步骤分为两步
1. 对元素进行hash 
2. 判断hash值在列表中是否存在，存在，判读元素本身值。

