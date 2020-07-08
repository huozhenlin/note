"""
什么是链表？熟悉python语法的同学肯定都知道list，但是这并不是真正意义上的链表（linked list）。链表是由一系列的节点(node)来实现的，
通过每一个node存储下一个节点的指针来实现一种快速的插入。此外每个节点都有一个cargo包含一定的数据。根据链表结构的不同，
其种类可以分为单向链表、单项循环链表、双向链表、双向循环链表等。

作者：taotianli
链接：https://juejin.im/post/5b93be37e51d450e68674833
来源：掘金
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
class Node:
    def __init__(self, dataval=None, nextval=None):
        self.dataval = dataval
        self.nextval = None



class SLinkedList:
    def __init__(self, headval=None):
        self.headval  = headval


    def append(self, newData):
        newNode = Node(newData)
        if not self.headval:
            self.headval = newNode

        last = self.headval
        while last.nextval:
            last = last.nextval

        last.nextval = newNode

    def show(self):
        printVal = self.headval
        while printVal:
            printVal = printVal.nextval
            print(printVal.dataval)
            print(printVal.nextval.dataval)


slinked = SLinkedList()
a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
slinked.headval = a
slinked.headval.nextval = b
b.nextval = c
slinked.append('F')
slinked.show()


