
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Sll:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        temp=self.head
        while temp:
            yield temp
            temp=temp.next

    def del_node(self,val:int) -> None:
        if not self.head:
            return 'SLL is empty!!'
        else:
            if self.head.data==val:
                if self.head==self.tail:
                    self.head=None
                else:
                    self.head = self.head.next
            else:
                prev =nxt= self.head
                while nxt.data != val:
                    prev=nxt
                    nxt=nxt.next
                    if not nxt:
                        print(f'{val} not found !!')
                        return
                print(f'{val} found !!')
                prev.next=nxt.next
                nxt=None
                return 'val deleted'


    def insert(self,val:int,location:int) -> None:
        new_node = Node(val)

        if not self.head:
            self.head=new_node
            self.tail=new_node
        else:
            if location==0:
                new_node.next=self.head
                self.head=new_node
            elif location==-1:
                self.tail.next=new_node
                self.tail=new_node
            else:
                cnt=0
                prev=nxt=self.head
                while cnt!=location:
                    cnt+=1
                    prev=nxt
                    nxt=nxt.next
                    if nxt is None:
                        break
                if nxt:
                    prev.next=new_node
                    new_node.next=nxt
                else:
                    self.tail.next = new_node
                    self.tail = new_node




if __name__=='__main__':
    sll = Sll()
    sll.insert(12,0)
    sll.insert(121,-1)
    sll.insert(122,-1)
    sll.insert(123,-1)
    sll.insert(124,-1)
    sll.insert(125,-1)
    sll.insert(100,0)
    print([n.data for n in sll])
    n=124
    print(f'\n{n} is going to be deleted.....\n')
    sll.del_node(n)
    print([n.data for n in sll])
