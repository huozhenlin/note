import pika
from threading import Thread
import traceback

username = 'zhenlin'  # 指定远程rabbitmq的用户名密码
pwd = 'zhenlin'
host = '192.168.1.76'
import time
import sys

class Producter():
    """
    消息队列生成者，初始化连接
    """

    def __init__(self, queue='', exchanage=''):
        self.conn = self.connect()
        self.quue = queue
        self.channel = self.conn.channel()
        self.exchanage = exchanage
        self.channel.queue_declare(queue=self.quue, durable=True)
        #开启confirm模式

    def connect(self):
        user_pwd = pika.PlainCredentials(username, pwd)
        connection = pika.BlockingConnection((pika.ConnectionParameters(host=host, credentials=user_pwd)))
        return connection

    def publish(self, routing_key, body):
        self.channel.basic_publish(exchange=self.exchanage,
                                   routing_key=routing_key,
                                   body=body)
        print("往交换机[%s]提交了数据:[%s]，路由关键字是:[%s]" % (self.exchanage, body, routing_key))

    def __del__(self):
        print('关闭生产者连接')
        self.conn.close()


class Consumer(Thread):
    """
    消息队列生成者，初始化连接
    """

    def __init__(self, queue='', exchanage=''):
        Thread.__init__(self)
        self.conn = self.connect()
        self.quue = queue
        self.channel = self.conn.channel()
        self.exchanage = exchanage
        self.channel.queue_declare(queue=self.quue, durable=True) #chi
        self.exception = None
        self.exc_traceback = ''

    def connect(self):
        user_pwd = pika.PlainCredentials(username, pwd)
        connection = pika.BlockingConnection((pika.ConnectionParameters(host=host, credentials=user_pwd)))
        return connection

    def callback(self, ch, method, properties, body):
        print(" [x] Received %r" % body)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def run(self):
        try:
           self.receive(self.quue)
        except Exception as e:
            print("有异常")
            self.exitcode = 1
            self.exception = e
            self.exc_traceback  = ''.join(traceback.format_exception(*sys.exc_info()))


    def receive(self, queue):
        try:
            self.channel.basic_consume(queue=queue,
                                       on_message_callback=self.callback,
                                       auto_ack=False)
            print(' [*] Waiting for messages. To exit press CTRL+C')
            self.channel.start_consuming()
            raise IOError
        except Exception as e:
            raise e


    def __del__(self):
        print('关闭消费者连接')
        self.conn.close()


if __name__ == '__main__':
    queue = 'message'
    # product = Producter(queue=queue)
    consumer = Consumer(queue=queue)
    consumer.start()
    consumer.join()
    if consumer.exception == 1:
        print('Exception in ' + consumer.getName() + ' (catch by main)')
        print(consumer.exc_traceback)

    # i = 0
    # message = 'hello_world_%s' % i
    # product.publish(queue, message)

    # while True:
    #     message = 'hello_world_%s'%i
    #     product.publish(queue,message)
    #     # Thread(target=product.publish, args=(queue, message)).start()
    #     # time.sleep(1)
    #     i +=1
