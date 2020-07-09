import time
import uuid
from threading import Thread
import redis
redis_cli = redis.Redis('localhost',6379, db=0)

# 获取一个分布式锁
def acquire_lock(lock_name, acquire_time=10, time_out=10):

    # 生成唯一的uuid
    identifine = str(uuid.uuid4())
    end = time.time() + acquire_time
    lock = "string:lock:" + lock_name
    while time.time() < end:
        # 旧版本方法，有bug
        # if redis_cli.setnx(lock, identifine):
        #     # 给锁设置超时时间，防止其他应用程序无非获取锁
        #     redis_cli.expire(lock, time_out)
        #     return identifine
        # elif not redis_cli.ttl(lock):
        #     redis_cli.expire(lock, time_out)

        # 新版本>=2.6.2, 原子操作
        if redis_cli.set(lock, identifine, ex=time_out, nx=True):
            return identifine
        # time.sleep(0.01)

    return False



#释放一个分布式锁
def release_lock(lock_name, identifine):
    lock = "string:lock:" + lock_name
    pip = redis_cli.pipeline(True)

    while True:
        pip.watch(lock)
        lock_value = redis_cli.get(lock)
        if not lock_value:
            return True

        # 判断是不是自己的锁，不是，放弃，是，直接释放
        if lock_value.decode() == identifine:
            # 开启事务，redis事务并非原子性，也就是说，一个步骤执行出错，不影响其他操作正常运行
            # redis 事务只是保证了进行当前事务时候，其他人的事务会等待，不会有新的数据操作
            pip.multi()
            pip.delete(lock)
            pip.execute()
            return True
        pip.unwatch()
        break

    return False


count = 10

def seckill(i):
    lock_name = 'resource'
    identifine = acquire_lock(lock_name)
    print("线程{}获得了锁".format(i))
    time.sleep(1)
    global count
    if count < 1:
        print("票剩余{}张，抢票失败".format(count))
        return

    count -=1
    print('线程{}抢到了一张票，还剩{}张票'.format(i, count))
    release_lock(lock_name, identifine)

for i in range(100):
    t = Thread(target=seckill, args=(i,))
    t.start()
