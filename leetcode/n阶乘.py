# assert list(filter(lambda x:x%4==0,range(19))) == [x for x in range(19) if x%4==0] # 过滤余数不为0


# method1
from functools import reduce

f = lambda x: x >=3 and f(x-1)+f(x-2) or 1 # 1,1,2,3,5,8,13....f(1000)? 时间复杂度：O(2^x) 空间复杂度O(x)

# method1 时间复杂度：O(2^x) 空间复杂度O(x)
# method2 时间复杂度：O(x) 空间复杂度O(1)


def fib1(x):
    """
     1,1,2,3,5,8,13....f(1000)?
    :param x:
    :return:
    """
    if x <3:
        return 1
    result = fib1(x-1)+fib1(x-2)
    return result

def fib2(x):
    """
     1,1,2,3,5,8,13....f(1000)?
    :param x:
    :return:
    """
    a1 = 1
    an = 1
    n = 3
    while n <= x:
        n +=1
        a1,an=an, an+a1

    return an

print ('1+100的总和是：%s' % reduce(lambda x,y:x+y,range(1,101)))
