class Stack(object):
    """栈类,用列表实现"""

    def __init__(self):
        self.__list = []
        # self.item = item

    def push(self, item):
        # 压栈
        self.__list.append(item)

    def pop(self):
        # 出栈
        return self.__list.pop()

    def peek(self):
        # 返回栈顶元素
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        # 判断是否为空
        return self.__list == []

    def size(self):
        # 返回栈的大小
        return len(self.__list)


if __name__ == '__main__':
    s = Stack()
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.peek())
    print(s.size())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.is_empty())
