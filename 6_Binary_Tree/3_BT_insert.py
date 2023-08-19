from collections import deque


class BT_Node:
    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None


class Binary_Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        node = BT_Node(data)
        if not self.root:
            self.root = node
        else:
            queue = deque([])
            queue.append(self.root)
            while len(queue) > 0:
                print([x.val for x in queue])
                tmp = queue.popleft()
                if tmp.left_child:
                    queue.append(tmp.left_child)
                else:
                    tmp.left_child = node
                    return
                if tmp.right_child:
                    queue.append(tmp.right_child)
                else:
                    tmp.right_child = node
                    return

    def in_order(self, node):
        if node:
            self.in_order(node.left_child)
            print((str(node.val)) + ' -> ', end='')
            self.in_order(node.right_child)


if __name__ == '__main__':
    bt = Binary_Tree()
    bt.insert(1)
    bt.insert(2)
    bt.insert(3)
    bt.insert(4)
    bt.insert(5)
    bt.insert(6)
    bt.insert(7)
    print('In-Order traversal --->')
    bt.in_order(bt.root)
