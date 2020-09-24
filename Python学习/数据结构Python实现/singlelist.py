class Node(object):
    """节点类"""
    def __init__(self, item):
        self.next = None
        self.item = item


class SingleLinkList(object):
    """ 链表类"""
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        # 判断链表是否为空
        return self.__head is None

    def length(self):
        # 返回链表的长度
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        # 遍历链表
        cur = self.__head
        while cur is not None:
            print(cur.item, end=' ')
            cur = cur.next
        print('')

    def add(self, item):
        # 在头部添加元素
        node = Node(item)
        node.next = self.__head
        self.__head = node


    def append(self, item):
        # 在末尾添加元素
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
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
            while count < position-1:
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        # 删除指定元素,使用一个游标
        cur = self.__head
        while cur is not None:
            if cur.item == item:
                self.__head = cur.next
                break
            elif cur.next.item == item:
                cur.next = cur.next.next
                break
            cur = cur.next


    def drop(self, item):
        # 删除第一次出现的指定元素，使用两个游标
        cur = self.__head
        if cur.item == item:
            self.__head = cur.next
        else:
            pre = cur
            cur = cur.next
            while cur is not None:
                if cur.item == item:
                    pre.next = cur.next
                    break
                pre = cur
                cur = cur.next



    def search(self, item):
        # 搜索指定元素
        cur = self.__head
        while cur is not None:
            if cur.item == item:
                print('找到了')
                break
            else:
                cur = cur.next
        print('没找到')


if __name__ == '__main__':
    l = SingleLinkList()
    # print(l.is_empty())
    l.append(1)
    l.append(2)
    l.append(3)
    l.append(4)
    l.append(5)
    l.travel()
    l.remove(5)
    l.travel()

