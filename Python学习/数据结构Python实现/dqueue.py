class Dqueue(object):
    """双端队列"""
    def __init__(self):
        self.__list = []

    def add_front(self, item):
        # 头部入队列
        self.__list.insert(0, item)

    def add_rear(self, item):
        # 头部入队列
        self.__list.append(item)

    def pop_rear(self):
        # 尾部出队列
        return self.__list.pop()

    def pop_front(self):
        # 尾部出队列
        return self.__list.pop(0)

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)