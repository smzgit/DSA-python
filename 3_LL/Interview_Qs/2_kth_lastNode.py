class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


# time complexity = O(n)
# space complexity = O(n)
def kth_last_node(head:Node, k:int) -> int :
    slow=head
    fast=head
    n=k
    while n>0 and fast:
        fast=fast.next
        n-=1

    while fast:
        slow=slow.next
        fast=fast.next
    print(f'{k} last node is {slow.data}')
    return

def print_sll(start:Node):
    while start:
        print(str(start.data)+' -> ',end='')
        start=start.next
    print()
if __name__ == '__main__':
    head=Node(12)
    head.next=Node(32)
    head.next.next=Node(42)
    head.next.next.next=Node(82)
    head.next.next.next.next=Node(12)
    head.next.next.next.next.next=Node(90)
    head.next.next.next.next.next.next=Node(190)

    kth_last_node(head,14)
    print_sll(head)