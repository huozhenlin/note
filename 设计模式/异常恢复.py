"""
通常，在一个链式调用的程序中，中途有一个环节出现问题了，那么，程序不捕获异常的话，直接崩溃，或者
捕获异常，一切重新开始
那么，异常恢复模式，相当于断点续传。也就意味着，它需要记录操作的步骤，当步骤完成后，标记为完成，
程序捕获异常的时候，重新开始，进行第一个步骤前，会先询问当前步骤是否已经完成，若完成，跳过，访问下
一个步骤，以此类推
"""

def a():
    print('a')

def b():
    print('b')

def c():
    print('c')

def d():
    print('d')


process = ['a', 'b', 'c', 'd']
i = 0
while True:
    print('执行次数%s'%i)
    if i> 10:
        break
    try:
        if 'a' in process:
            a()
            process.remove('a')

        if 'b' in process:
            b()
            if i >= 5:
                process.remove('b')

            raise Exception

        if 'c' in process:
            c()
            process.remove('c')

        if 'd' in process:
            d()
            process.remove('d')
            break
    except Exception as e:
        i+=1
        print(e.args)