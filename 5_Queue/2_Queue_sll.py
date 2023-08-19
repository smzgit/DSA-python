class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        

class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def is_empty(self):
        return not self.head
    
    def enque(self,val):
        new_node=Node(val)
        if not self.head:
            self.head=new_node
            self.tail=self.head
        else:
            self.tail.next=new_node
            self.tail=new_node

    def deque(self):
        if self.is_empty():
            print('Queue is empty!!')
            return
        else:
            tmp=self.head.val
            self.head=self.head.next
            return tmp
            
    def print_q(self):
        if self.is_empty():
            print('Queue is empty!!')
            return 
        else:
            tmp=self.head
            while tmp:
                print(str(tmp.val)+' - ',end='')
                tmp=tmp.next
            print()

    def peek(self):
        if self.is_empty():
            print('Queue is empty!!')
            return
        return self.head.val

    def del_que(self):
        self.head=None
        self.tail=None
        print('whole queue deleted !!')
        return



if __name__ == '__main__':
    q = Queue()
    print('is q empty??\nans -> ',q.is_empty())
    q.enque(12)
    q.enque(51)
    q.enque(89)
    q.enque(100)
    q.print_q()

    q.deque()
    q.print_q()
    q.deque()
    q.print_q()
    q.enque(2131)
    q.enque(931)
    q.enque(31)
    q.enque(211)
    q.print_q()
    print('\nPeek element = ',q.peek())

    q.del_que()
