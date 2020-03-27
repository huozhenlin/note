import time
a=['apple', 'banana', 'apple', 'tomato', 'orange', 'apple', 'banana', 'watermeton']


def get_time_stamp():
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s.%03d" % (data_head, data_secs)
    stamp = ("".join(time_stamp.split()[0].split("-")) + "".join(time_stamp.split()[1].split(":"))).replace('.', '')
    return int(stamp)


#计算时间函数
def print_run_time(func):
    def wrapper(*args, **kw):
        local_time = get_time_stamp()
        func(*args, **kw)
        print('current Function [%s] run time is %.2f' % (func.__name__ , get_time_stamp() - local_time))
    return wrapper

#方法一
@print_run_time
def method1():
    i = 0
    j=1
    a_count = {}
    while i < len(a):
        while j < len(a):
            if not a_count.get(a[j]):
                a_count[a[j]] = 1
            if a[j] == a[i]:
                a_count[a[j]] += 1
                a.pop(j)
                j -= 1
            j += 1
        i+=1
        j = i+1

    print(a_count)


@print_run_time
def method2():
    from collections import Counter
    c = Counter()
    for i in a:
        c[i] += 1
    print(c)

method1()
# method2()