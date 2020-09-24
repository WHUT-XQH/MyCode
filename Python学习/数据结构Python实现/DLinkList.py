
class Node(object):
    """节点类"""
    def __init__(self, item):
        self.item = item
        self.next = None
        self.pre = None


class DLinkList(object):
    """双链表类"""

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
        node.next.pre = node

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
            node.pre = cur

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
            count = 0
            cur = self.__head
            while count < position:
                count += 1
                cur = cur.next
            node.next = cur
            node.pre = cur.pre
            cur.pre.next = node
            cur.pre = node

    def remove(self, item):
        # 删除指定元素
        cur = self.__head
        while cur is not None:
            if cur.item == item:
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next is not None:
                        cur.next.pre = None
                    break
                else:
                    cur.pre.next = cur.next
                    if cur.next is not None:
                        cur.next.pre = cur.pre
                    break
            else:
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
    l = DLinkList()
    # print(l.is_empty())
    l.append(1)
    l.append(2)
    l.append(3)
    l.append(4)
    l.append(5)
    l.travel()
    #l.remove(5)
    #l.append(6)
    l.insert(4,6)
    l.travel()



