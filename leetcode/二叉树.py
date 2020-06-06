class TreeNode:

    def __init__(self, x):
        self.val = x
        self.Left = None
        self.Right = None


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
a.Left = b
a.Right = c
b.Left = d
b.Right = e
c.Left = f
c.Right = g

def preOrderTraversebyRecursive(node):
    # 前序遍历, 递归实现
    if not node:
        return None
    # print(node.val)
    preOrderTraversebyRecursive(node.Left)
    preOrderTraversebyRecursive(node.Right)

def preOrderTraverseNotbyRecursive(node):

    stack = [node]
    while len(stack) > 0:
        # print(node.val)
        if node.Right:
            stack.append(node.Right)

        if node.Left:
            stack.append(node.Left)

        node = stack.pop()

def inOrderTraversebyRecursive(node):
    # 前序遍历, 递归实现
    if not node:
        return None
    preOrderTraversebyRecursive(node.Left)
    # print(node.val)
    preOrderTraversebyRecursive(node.Right)

def postOrderTraversebyRecursive(node):
    # 前序遍历, 递归实现
    if not node:
        return None
    preOrderTraversebyRecursive(node.Left)
    # print(node.val)
    preOrderTraversebyRecursive(node.Right)

def layerTraverse(node):
    _queue = list()
    _queue.append(node)
    while len(_queue) > 0:
        tmp = _queue.pop(0)
        print(tmp.val)
        if node.Left:
            _queue.append(tmp.Left)

        if node.Right:
            _queue.append(tmp.Right)


layerTraverse(a)