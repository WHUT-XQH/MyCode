class Queue(object):
    """队列类"""
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        # 入队列
        self.__list.insert(0, item)

    def dequeue(self):
        # 出队列
        return self.__list.pop()

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)

if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.size())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())


