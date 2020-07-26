import pika

import uuid

username = 'zhenlin'  # 指定远程rabbitmq的用户名密码
pwd = 'zhenlin'
host = '192.168.1.76'
class RpcClient(object):

    def __init__(self):
        user_pwd = pika.PlainCredentials(username, pwd)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, credentials=user_pwd))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True, queue='rpc_queue')

        self.callback_queue = result.method.queue
        print(self.callback_queue)

        self.channel.basic_consume(on_message_callback=self.on_response, auto_ack=True,
                                        queue=self.callback_queue
                                  )

    def on_response(self, ch, method, props, body):

        if self.corr_id == props.correlation_id:
            self.response = {"body":body, "result":self.fil(body)}


    def fil(self,n):
        a1 = 1
        an = 1
        i = 3
        while i <= int(bytes.decode(n)):
            i+=1
            a1,an= an, an+a1

        return an


    def call(self, n):

        self.response = None

        self.corr_id = str(uuid.uuid4())

        self.channel.basic_publish(exchange='',

                                   routing_key='rpc_queue',

                                   properties=pika.BasicProperties(

                                       reply_to=self.callback_queue,

                                       correlation_id=self.corr_id,

                                   ),

                                   body=str(n))

        while self.response is None:
            self.connection.process_data_events()

        return str(self.response)


rpc = RpcClient()

print(" [x] Requesting")

response = rpc.call(100)

print(" [.] Got %r" % response)