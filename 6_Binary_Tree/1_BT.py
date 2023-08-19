class BT_Node:
    def __init__(self,val):
        self.val=val
        self.left_child=None
        self.right_child=None

class Binary_Tree:
    def __init__(self,root):
        self.root=root

    def pre_order(self,node):
        if node:
            print(str(node.val) + ' -> ', end='')
            self.pre_order(node.left_child)
            self.pre_order(node.right_child)

    def in_order(self,node):
        if node:

            self.in_order(node.left_child)
            print(str(node.val) + ' -> ', end='')
            self.in_order(node.right_child)

    def post_order(self,node):
        if node:
            self.post_order(node.left_child)
            self.post_order(node.right_child)
            print(str(node.val) + ' -> ', end='')


if __name__ == '__main__':
    b_tree=BT_Node(1)
    b_tree.left_child=BT_Node(2)
    b_tree.left_child.left_child=BT_Node(4)
    b_tree.left_child.right_child=BT_Node(5)

    b_tree.right_child=BT_Node(3)
    b_tree.right_child.left_child=BT_Node(6)
    b_tree.right_child.right_child=BT_Node(7)

    my_tree=Binary_Tree(b_tree)
    print('PRE-ORDER TRAVERSAL ----------->')
    my_tree.pre_order(b_tree)
    print('\nIN-ORDER TRAVERSAL ----------->')
    my_tree.in_order(b_tree)
    print('\nPOST-ORDER TRAVERSAL ----------->')
    my_tree.post_order(b_tree)
