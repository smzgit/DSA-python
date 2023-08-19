'''
Question 3 - Partition a linked list around value x such that all nodes less
             than x comes before all nodes greater than or equal to x.
'''

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


# time complexity = O(n)
# space complexity = O(n)
def partition_sll(head:Node,x:int):

    left=Node(-1)
    l_pt=left
    right=Node(-1)
    r_pt = right
    tmp=head
    while tmp:
        if tmp.data<x:
            l_pt.next=tmp
            l_pt=l_pt.next
        else:
            r_pt.next=tmp
            r_pt=r_pt.next
        tmp=tmp.next

    r_pt.next = None
    l_pt.next=right.next
    return left.next


def print_sll(start:Node):
    while start:
        print(str(start.data)+' -> ',end='')
        start=start.next
    print()

if __name__ == '__main__':
    head=Node(10)
    head.next=Node(4)
    head.next.next=Node(20)
    head.next.next.next=Node(10)
    head.next.next.next.next=Node(3)


    print_sll(head)
    print_sll(partition_sll(head,3))