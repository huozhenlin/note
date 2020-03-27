from functools import wraps


def quick_sort(func):
    """
    快速排序，也就是小于第一个数的放一边，大于另一个数的放另一遍，循环递归调用
    """
    @wraps(func)
    def inner_func(*args, **kwargs):
        target = kwargs.get('target')
        sored_list = kwargs.get('list')
        if not target:
            sored_list = args[0]
            target = args[1]

        def _tosorted(list):
            if len(list) <= 1:
                return list
            else:
                start = list[0]
                before = [i for i in list[1:] if i < start]
                after = [i for i in list[1:] if i > start]
                final = _tosorted(before) + [start] + _tosorted(after)
            return final
        return func( _tosorted(sored_list), target)
    return inner_func


@quick_sort
def find(list, target):
    """二分查找，只能在有序列表中查找目标值.
    思想：
    1：获取初始值和数组长度，分别赋值给low,hight
    2:当low<=hight时，循环比较
        1：当中间值小于目标值时，将最小值的下标改成中间值下标+1
        2：当中间值大于目标值时，将最大值的下标改成中间值下标+1
        3：判断中间值和目前值是否相等，返回结果
    """
    low = 0
    high = len(list)-1
    if len(list) == 0 :
        return
    count = 0
    print(list)
    while low <= high:
        count += 1
        print('查找次数',count )
        mid = int((high - low) / 2)+low
        _num = list[mid]
        if _num > target:
            high = mid - 1
        elif _num < target:
            low = mid + 1
        else:
            print('找到结果')
            return mid

    print('找不到结果')

find([1,5,2,3,10,6,7,8,99,100,45], 100)