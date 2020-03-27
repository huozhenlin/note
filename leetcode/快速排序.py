"""
快速排序，也就是小于第一个数的放一边，大于另一个数的放另一遍，循环递归调用
"""
def quick_sort(list):
    if len(list) <= 1:
        return list
    else:
        start = list[0]
        before = [i for i in list[1:] if i < start]
        after = [i for i in list[1:] if i > start]
        final = quick_sort(before) +[start] + quick_sort(after)

    return final

print(quick_sort([1,5,2,7,0,5]))