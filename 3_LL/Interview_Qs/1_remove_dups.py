class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


# time complexity = O(n)
# space complexity = O(n)
def remove_duplicates(start:Node):
    node_set = set()
    node_set.add(start.data)
    tmp=start
    while tmp.next:
        if tmp.next.data in node_set:
            tmp.next = tmp.next.next
        else:
            node_set.add(tmp.data)
            tmp=tmp.next

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
    head.next.next.next.next.next.next=Node(12)

    print_sll(start=head)
    remove_duplicates(start=head)
    print_sll(start=head)

