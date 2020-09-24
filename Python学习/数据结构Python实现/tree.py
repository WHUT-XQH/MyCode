class Node(object):
    def __init__(self, item):
        self.item = item
        self.left_child = None
        self.right_child = None


class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.left_child is None:
                cur_node.left_child = node
                return
            else:
                queue.append(cur_node.left_child)
            if cur_node.right_child is None:
                cur_node.right_child = node
                return
            else:
                queue.append(cur_node.right_child)

    def breadth_travel(self):
        """广度遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.item, end='')
            if cur_node.left_child is not None:
                queue.append(cur_node.left_child)
            if cur_node.right_child is not None:
                queue.append(cur_node.right_child)

    def preorder(self, node):
        """先序遍历"""
        if node is None:
            return
        print(node.item, end='')
        self.preorder(node.left_child)
        self.preorder(node.right_child)

    def midorder(self, node):
        """中序遍历"""
        if node is None:
            return
        self.midorder(node.left_child)
        print(node.item, end='')
        self.midorder(node.right_child)

    def backorder(self, node):
        """后序遍历"""
        if node is None:
            return
        self.backorder(node.left_child)
        self.backorder(node.right_child)
        print(node.item, end='')



if __name__ == '__main__':
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print('')
    tree.preorder(tree.root)
    print('')
    tree.midorder(tree.root)
    print('')
    tree.backorder(tree.root)
