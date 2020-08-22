# 装饰器作用
装饰器主要是用来包装函数，对于一些常用的功能，譬如：日志打印，函数计时，身份认证。我们可以使用装饰器来实现，这样可以降低整个程序的复杂度和减少程序的代码量。

它实际上就是函数，不同的是，它把一个函数当做参数，然后返回一个替代版函数。

# 如何定义一个装修器
1. 带参数装饰器  
```python
import sys
import os
import traceback
import logging
from logging.handlers import TimedRotatingFileHandler
import time
log_dir1 = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
today = time.strftime('%Y%m%d', time.localtime(time.time()))
full_path = os.path.join(log_dir1, today)
if not os.path.exists(full_path):
    os.makedirs(full_path)


# 带参数的装饰器需要2层装饰器实现,第一层传参数，第二层传函数，每层函数在上一层返回
def loggerInFile(filename):
    def decorator(func):
        def inner(*args, **kwargs):  # 1
            logFilePath = os.path.join(log_dir1,filename)  # 日志按日期滚动，保留5天
            logger = logging.getLogger()
            logger.setLevel(logging.ERROR)

            # 文件日志
            handler = TimedRotatingFileHandler(logFilePath,
                                               when="d",
                                               interval=1,
                                               backupCount=5)
            formatter = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)


            # 控制台日志
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.formatter = formatter  # 也可以直接给formatter赋值
            console_handler.setLevel(logging.INFO)

            # 为logger添加的日志处理器
            logger.addHandler(console_handler)
            logger.addHandler(handler)

            try:
                result = func(*args, **kwargs)
                logger.info(result)
            except:
                logger.error(traceback.format_exc())

        return inner

    return decorator
```
2. 无参数装修器  
```python
# 无参数实现
def logger(func):
    def inner(*args, **kwargs):  # 1
        try:
            func(*args, **kwargs)  # 2
        except:
            print('error')

    return inner

```
# 装饰器调用
```python

@loggerInFile('test.log')
def test(n):
    return(100/n)
    
@logger
def test(n):
    return(100/n)
    
```  
