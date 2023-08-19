class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None

class doubly_LL:
    def __init__(self):
        self.head=None
        self.tail=None

    def insert(self,data,loc):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            self.tail=new_node
        else:
            if loc==0:
                new_node.next=self.head
                self.head.prev=new_node
                self.head=new_node
            elif loc==-1:
                self.tail.next=new_node
                new_node.prev=self.tail

                self.tail=new_node
            else:
                ind=0
                tmp=self.head
                while ind<loc-1:
                    tmp=tmp.next
                    ind+=1
                new_node.next=tmp.next
                tmp.next.prev=new_node
                new_node.prev=tmp
                tmp.next=new_node


    def print_dll(self):
        tmp = self.head
        while tmp:
            print(str(tmp.val)+'->',end='')
            tmp=tmp.next
        print()

    def reverse_print_dll(self):
        tmp = self.tail
        while tmp:
            print(str(tmp.val) + '->',end='')
            tmp = tmp.prev
        print()

    def del_node(self,val):
        prev = self.head
        nxt = prev.next
        if self.head.val==val:
            tmp=self.head
            tmp.next.prev = None
            self.head=tmp.next
            tmp.next = None
            print(f'{val} deleted from the DLL [HEAD]')
            return
        elif self.tail.val==val:
            tmp = self.tail.prev
            tmp.next = None
            self.tail.prev = None
            self.tail=tmp
            print(f'{val} deleted from the DLL [TAIL]')
            return
        while nxt:
            if val == nxt.val:
                nxt.next.prev=nxt.prev
                prev.next=nxt.next
                print(f'{val} deleted from the DLL')
                return
        prev=nxt
        nxt = nxt.next
        print(f'{val} is not present in DLL')
        return

    def search_node(self,val):
        tmp = self.head
        while tmp:
            if val==tmp.val:
                print(f'{val} is present in DLL')
                return
            tmp=tmp.next
        print(f'{val} is not present in DLL')
        return


if __name__ == '__main__':
    dll = doubly_LL()
    dll.insert(1,0)
    dll.insert(2,-1)
    dll.insert(3,-1)
    dll.insert(4,-1)
    dll.insert(100,2)
    # dll.print_dll()
    # dll.reverse_print_dll()
    # dll.search_node(1080)

    dll.del_node(1)
    dll.print_dll()
    dll.reverse_print_dll()