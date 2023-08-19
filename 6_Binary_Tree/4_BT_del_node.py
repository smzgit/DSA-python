class BT_Node:
    def __init__(self,data):
        self.val=data
        self.left_child=None
        self.right_child=None

class Binary_Tree:
    def __init__(self,root):
        self.root=root

    def get_deepestNode(self,root):
        if not root:
            return
        else:
            from collections import deque
            q = deque([])
            q.append(root)
            while len(q)>0:
                print([x.val for x in q])
                node=q.popleft()
                if node.left_child:
                    q.append(node.left_child)
                if node.right_child:
                    q.append(node.right_child)

            return node


    def del_deepNode(self,node,dnode):
        if node:
            if node is dnode:
                node=None
            else:
                if node.left_child is dnode:
                    node.left_child=None
                if node.right_child is dnode:
                    node.right_child=None
            self.del_deepNode(node.left_child,dnode)
            self.del_deepNode(node.right_child,dnode)

    def del_Node(self,node,data):
        if node:
            if node.val==data:
                print('val found!!')
                deep_node=self.get_deepestNode(self.root)
                node.val=deep_node.val
                self.del_deepNode(self.root,deep_node)
                return
            self.del_Node(node.left_child,data)
            self.del_Node(node.right_child,data)

    def in_order(self, node):
        if node:
            self.in_order(node.left_child)
            print((str(node.val)) + ' -> ', end='')
            self.in_order(node.right_child)


if __name__ == '__main__':
    b_tree=BT_Node(1)
    b_tree.left_child=BT_Node(2)
    b_tree.left_child.left_child=BT_Node(4)
    b_tree.left_child.right_child=BT_Node(5)
    b_tree.left_child.right_child.left_child=BT_Node(8)
    b_tree.left_child.right_child.left_child.right_child=BT_Node(9)

    b_tree.right_child=BT_Node(3)
    b_tree.right_child.left_child=BT_Node(6)
    b_tree.right_child.right_child=BT_Node(7)

    binary_tree = Binary_Tree(b_tree)
    print()
    # deep=binary_tree.get_deepestNode(b_tree)
    # print('deepest node = ',deep.val)
    # binary_tree.del_deepNode(b_tree,deep)
    #
    # print('Inorder --->')
    binary_tree.in_order(b_tree)
    n=4
    print('\ndeleting node ',n)
    print(binary_tree.del_Node(b_tree,n))
    # print('Inorder --->')
    binary_tree.in_order(b_tree)



