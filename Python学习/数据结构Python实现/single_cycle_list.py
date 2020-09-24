class Node(object):
    """节点类"""
    def __init__(self, item):
        self.next = None
        self.item = item


class SingleCycleLinkList(object):
    """ 链表类"""
    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        # 判断链表是否为空
        return self.__head is None

    def length(self):
        # 返回链表的长度
        cur = self.__head
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        # 遍历链表
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.item, end=' ')
            cur = cur.next
        print(cur.item)

    def add(self, item):
        # 在头部添加元素
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            self.__head = node
            cur.next = node

    def append(self, item):
        # 在末尾添加元素
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            cur.next = node

    def insert(self, position, item):
        # 插入元素到指定位置
        node = Node(item)
        if position <= 0:
            self.add(item)
            print('位置小于0，已在头部添加')
        elif position > (self.length()-1):
            self.append(item)
            print('位置超出范围，已在尾部添加')
        else:
            pre = self.__head
            count = 0
            while count < position - 1:
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        # 删除指定元素
        if self.is_empty():
            return
        cur = self.__head
        if self.__head.item == item:
            if self.length() == 1:
                self.__head = None
                return
            else:
                while cur.next != self.__head:
                    cur = cur.next
                self.__head = cur.next.next
                cur.next = cur.next.next
                return
        else:
            while cur.next != self.__head:
                if cur.next.item == item:
                    cur.next = cur.next.next
                    return
                cur = cur.next
            print('未找到指定元素')




    def search(self, item):
        # 搜索指定元素
        if self.is_empty():
            print('空的，不用找了')
            return
        cur = self.__head
        while cur.next != self.__head:
            if cur.item == item:
                print('找到了')
                return
            else:
                cur = cur.next
        if cur.item == item:
            print('找到了')
        print('没找到')


if __name__ == '__main__':
    l = SingleCycleLinkList()
    # print(l.is_empty())
    l.append(1)
    # l.append(2)
    # l.append(3)
    # l.append(4)
    # l.append(5)
    l.travel()
    print('haole')
    l.remove(1)
    l.travel()




