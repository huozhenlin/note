import threading


class Account():
    """
    线程的生命周期
    创建->就绪->运行->等待/阻塞->死亡
    new关键字创建线程，
    run关键字时线程进入就绪状态，具体执行由cpu分配
    使用wait/join会让当前线程或其他进程进入阻塞状态
    任务执行完毕，线程进入销毁死亡状态
    """

    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance
        self.rlock = threading.RLock() # 锁对象


    def get_balance(self):
        """
        查询余额操作
        :return:
        """
        return self.balance

    def draw(self, draw_amount):
        self.rlock.acquire() # 加锁
        print("加锁")
        try:
            if draw_amount <= self.balance:
                print("从账号取出RMB{}".format(draw_amount))
                self.balance = self.balance - draw_amount
                print("余额{}".format(self.get_balance()))

            else:
                print("余额不足")
        except Exception as e:
            print(e.args)
        finally:
            self.rlock.release()
            print("锁释放")


ming = Account('0001',50000)
threading.Thread(name="0", target=ming.draw, args=(800,)).start()
threading.Thread(name="0", target=ming.draw, args=(80000,)).start()
threading.Thread(name="0", target=ming.draw, args=(800,)).start()
threading.Thread(name="0", target=ming.draw, args=(800,)).start()










