"""
python 优先队列实现有三种方式
第一种：list，写入tunple,然后sort,时间复杂度为O(n)
第二种：heapq, 底层实现也是list，不过可以实现nlogn的时间复杂度
第三章：使用queue中的PriorityQueue,内部实现是使用了heapq，区别是，heapq非线程安全，
PriorityQueue为线程安全，提供锁机制

                                   0

                  1                                 2

          3               4                5               6

      7       8       9       10      11      12      13      14

    15 16   17 18   19 20   21 22   23 24   25 26   27 28   29 30

2k-1 root 2k+1 索引

参考资料：yangyanxing.com/article/priorityqueue_in_python.html
"""


#第一种方法实现
my_queue = []
# my_queue.append((1,'a'))
# my_queue.append((9,'b'))
# print(my_queue)
# my_queue.sort(key=lambda x:x[0], reverse=True)
# print(my_queue)
# my_queue.append((2,'b'))
# my_queue.append((3,'c'))
# print(my_queue)
# my_queue.sort(key=lambda x:x[0], reverse=True)
# print(my_queue)

# 第二种方法实现
# import heapq
# heapq.heappush(my_queue,(-1,'a'))
# heapq.heappush(my_queue,(-10,'c'))
# heapq.heappush(my_queue,(-9,'d'))
# heapq.heappush(my_queue,(-14,'g'))
# while my_queue:
#     task = heapq.heappop(my_queue)
#     print(task[0],task[1])

# 第三种方法实现
# from queue import PriorityQueue
#
# pq = PriorityQueue()
# pq.put((1,'a'))
# pq.put((6,'i'))
# pq.put((3,'g'))
# pq.put((4,'e'))
# while pq.qsize() !=0:
#     print(pq.get_nowait())
