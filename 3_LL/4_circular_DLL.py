class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None


class circular_dll:
    def __init__(self):
        self.head=None
        self.tail=None

    def insert(self,data,loc):
        new_node=Node(data)

        if not self.head:
            self.head=new_node
            self.tail=new_node
            new_node.next=self.head
            new_node.prev=self.tail
        else:
            if loc==0:
                new_node.next=self.head
                new_node.prev=self.tail

                self.tail.next=new_node
                self.head.prev=new_node

                self.head=new_node
            elif loc==-1:
                new_node.next=self.head
                new_node.prev=self.tail

                self.head.prev=new_node
                self.tail.next=new_node
                self.tail=new_node
            else:
                ind=0
                tmp=self.head
                while ind<loc-1:
                    ind+=1
                    tmp=tmp.next
                new_node.next=tmp.next
                tmp.next.prev=new_node
                new_node.prev=tmp
                tmp.next=new_node



    def print_circular_dll(self):
        tmp=self.head
        while tmp:
            print(str(tmp.val)+' -> ',end='')
            tmp=tmp.next
            if tmp==self.head:
                break
        print()
    def reverse_circular_dll(self):
        tmp = self.tail
        while tmp:
            print(str(tmp.val) + ' -> ', end='')
            tmp = tmp.prev
            if tmp==self.tail:
                break
        print()


    def search_node(self,data):
        tmp=self.head.next
        while tmp!=self.head:
            if tmp.val==data:
                print('{} present in the doubly CLL'.format(data))
                return
            tmp=tmp.next
        print(f'{data} not present in the doubly CLL')
        return

    def del_node(self,data):
        if not self.head:
            print("DCLL is empty!!")
            return
        if self.head.val==data:
            self.tail.next=self.head.next
            self.head.next.prev=self.tail
            self.head=self.head.next
            print(f'{data} deleted from DCLL')
            return
        if self.tail.val==data:
            self.tail.prev.next=self.head
            self.head.prev=self.tail.prev

            self.tail=self.tail.prev
            print(f'{data} deleted from DCLL')
            return
        else:
            prv=self.head
            nxt=self.head.next

            while prv.next!=self.head:
                if nxt.val==data:
                    prv.next = nxt.next
                    nxt.next.prev = prv
                    print(f'{data} deleted from DCLL')
                    return
                prv=nxt
                nxt=nxt.next

        print(f'{data} not present the in DCLL')
        return


if __name__ == '__main__':
    c_dll=circular_dll()
    c_dll.insert(1,0)
    c_dll.insert(2,-1)
    c_dll.insert(3,-1)
    c_dll.insert(4,-1)
    c_dll.insert(5,-1)
    c_dll.insert(6,-1)
    c_dll.insert(7,-1)
    c_dll.insert(8,-1)

    c_dll.insert(12,0)
    c_dll.insert(13,0)
    c_dll.insert(14,0)

    print('---------------------------------------\n')
    c_dll.print_circular_dll()
    c_dll.reverse_circular_dll()
    c_dll.search_node(8)
    print('---------------------------------------\n')
    c_dll.del_node(11)
    c_dll.print_circular_dll()
    c_dll.reverse_circular_dll()
    print('---------------------------------------\n')
    c_dll.insert(989,5)
    c_dll.print_circular_dll()
    c_dll.reverse_circular_dll()
