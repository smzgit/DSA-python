class BT_Node:
    def __init__(self,val,level=0):
        self.val=val
        self.left_child=None
        self.right_child=None
        self.level=level

    def __str__(self):
        return str(self.val)

class Binary_Tree:
    op=[]
    def __init__(self,root):
        self.root=root
        self.max_level=0

    def print_level(self,root,l):
        if root :
            self.print_level(root.left_child,l)
            if  root.level==l:
                print(str(root.val)+ ' -> ', end='')
            self.print_level(root.right_child,l)

    def level_order(self,node):
        print('\nLevel order traversal using height of tree -->')
        for i in range(1,4):
                self.print_level(node,i)

    def add_level(self,root,l):
        if root:
            self.add_level(root.left_child,l=l+1)
            root.level=l
            self.add_level(root.right_child,l=l+1)

    def in_order(self,node):
        if node:

            self.in_order(node.left_child)
            print((str(node.level)+','+str(node.val)) + ' -> ', end='')
            self.in_order(node.right_child)

    def simple_level_order(self,node):
        print(Binary_Tree.op)
        ans=[]
        leftview = self.left_view(node=node,level=1,left_nodes=[])
        print("\n\nLEFT VIEW OF TREE =>")
        print(leftview)
        if node:
            from collections import deque
            queue = deque([])
            queue.append(node)
            while len(queue)>0:

                temp = queue.popleft()
                #ans.append(temp.val)

                print(str(temp.val) + ' -> ', end='')
                if temp.val in leftview:
                    ans.append([temp.val])
                    print(ans)
                else:
                    ans[-1].append(temp.val)
                if temp.left_child:
                    queue.append(temp.left_child)
                if temp.right_child:
                    queue.append(temp.right_child)
        print()
        print(ans)

    def left_view(self,node,level,left_nodes):
        if node:
            print('Level = ', level, ' Max level = ',self.max_level, ' Node val = ', node.val)
            if level>self.max_level:
                self.max_level=level
                left_nodes.append(node.val)

            self.left_view(node.left_child,level+1,left_nodes)
            self.left_view(node.right_child,level+1,left_nodes)
        return left_nodes



if __name__ == '__main__':
    b_tree=BT_Node(1)
    b_tree.left_child=BT_Node(2)
    b_tree.left_child.left_child=BT_Node(4)
    b_tree.left_child.right_child=BT_Node(5)

    b_tree.right_child=BT_Node(3)
    b_tree.right_child.left_child=BT_Node(6)
    b_tree.right_child.left_child.left_child=BT_Node(60)
    b_tree.right_child.left_child.right_child=BT_Node(90)
    b_tree.right_child.right_child=BT_Node(7)

    my_bt = Binary_Tree(b_tree)
    my_bt.add_level(b_tree,l=1)
    my_bt.in_order(b_tree)

    my_bt.level_order(b_tree)

    print('\nsimple level order traversal using Queue ->')
    my_bt.simple_level_order(b_tree)
    # ans=my_bt.left_view(node=b_tree,level=1,left_nodes=[])
    # print('\nLeft View =>')
    # print(ans)

