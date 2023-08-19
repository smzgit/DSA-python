class Tree_Node:
    def __init__(self,data):
        self.val=data
        self.left_child=None
        self.right_child=None

class BST:
    def __init__(self):
        self.root=None

    def insert_node(self,data):
        new_node = Tree_Node(data)
        if not self.root:
            self.root=new_node
        else:
            first=self.root
            while True:
                last=first
                if first.val > data:
                    first=first.left_child
                    if not first:
                        last.left_child=new_node
                        break
                else:
                    first = first.right_child
                    if not first:
                        last.right_child = new_node
                        break

    def get_min_successor(self,node):
        tmp=node
        while tmp.left_child:
            tmp=tmp.left_child
        return tmp

    def del_node(self,rootNode, nodeValue):
        if rootNode is None:
            return rootNode
        if nodeValue < rootNode.val:
            rootNode.left_child = self.del_node(rootNode.left_child, nodeValue)
        elif nodeValue > rootNode.val:
            rootNode.right_child = self.del_node(rootNode.right_child, nodeValue)
        else:
            if rootNode.left_child is None:
                # temp = rootNode.right_child
                # rootNode = None
                return rootNode.right_child

            if rootNode.right_child is None:
                # temp = rootNode.left_child
                # rootNode = None
                return rootNode.left_child

            temp = self.get_min_successor(rootNode.right_child)
            rootNode.val = temp.val
            rootNode.right_child = self.del_node(rootNode.right_child, temp.val)
        return rootNode

    def deleteBST(rootNode):
        rootNode.val = None
        rootNode.left_child = None
        rootNode.right_child = None
        return "The BST has been successfully deleted"


    def pre_order(self,node):
        if node:
            print(str(node.val)+' -> ',end='')
            self.pre_order(node.left_child)
            self.pre_order(node.right_child)


    def search_node(self,node,data):
        if node:
            if node.val == data :
                print(f'{data} found !!')
                return data
            if data < node.val:
                self.search_node(node.left_child,data)
            if data > node.val:
                self.search_node(node.right_child, data)



if __name__ == '__main__':
    bst = BST()
    bst.insert_node(70)
    bst.insert_node(90)
    bst.insert_node(50)
    bst.insert_node(30)
    bst.insert_node(80)
    bst.insert_node(100)
    bst.insert_node(60)
    bst.insert_node(20)
    bst.insert_node(40)
    print('\nInorder traversal of BST -->')
    bst.pre_order(bst.root)
    print('\n---------------------------------------------')
    n=210
    print(f'searching {n} in bst....')
    bst.search_node(bst.root,n)

    del_num=40
    bst.del_node(bst.root,del_num)
    print(f'{del_num} deleted !!')
    print('\nInorder traversal of BST -->')
    bst.pre_order(bst.root)


















