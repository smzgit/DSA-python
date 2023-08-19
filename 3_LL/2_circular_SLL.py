class Node:
    def __init__(self,data):
        self.val=data
        self.next=None


class circular_SLL:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        temp=self.head
        while temp:
            yield temp
            temp=temp.next
            if temp==self.tail.next:
                break

    def create_c_sll(self,val):
        new_node=Node(val)
        new_node.next=new_node
        self.head=new_node
        self.tail=new_node

    def insert(self,val,loc):
        new_node=Node(val)

        if not self.head:
            return 'circular SLL is empty'
        else:
            if loc==0:
                new_node.next=self.head
                self.head=new_node
                self.tail.next=new_node
            elif loc==-1:
                self.tail.next = new_node
                new_node.next=self.head
                self.tail=new_node
            else:
                temp=self.head
                ind=0
                while ind<loc-1:
                    temp=temp.next
                    ind+=1

                new_node.next=temp.next
                temp.next=new_node




c_sll = circular_SLL()
c_sll.create_c_sll(1)
c_sll.insert(2,-1)
c_sll.insert(3,-1)
c_sll.insert(4,-1)
c_sll.insert(5,-1)
c_sll.insert(6,5)
print([v.val for v in c_sll])