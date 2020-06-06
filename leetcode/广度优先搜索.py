from collections import deque


def person_is_seller(name):
    print(name[0])
    return name[0] == 'm'  # 如果这个名字是以M结尾，则是


def search(name):
    graph = {}
    graph['you'] = ['alice', 'bob', 'mar', 'rain', 'cat'] #散列表

    search_queue = deque()  # 创建一个队列
    search_queue += graph['you']  # 将you压入队列

    search_queue += graph[name]  # 将需要查找的压入队列

    searched = []  # 用于记录已经查找过的
    while search_queue:  # 只要队列不为空

        person = search_queue.popleft()  # 取出左边第一个人

        if not person in searched:  # 当这个人不在searched中才继续往下查找

            if person_is_seller(person):  # 检查这个人是否为芒果商
                print(person, 'is manguoshang')
                return True
            else:
                search_queue += graph[person]  # 将这个人的朋友加入队列
                searched.append(person)
    return False  # 没有芒果商


search('mar')
