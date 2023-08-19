class Node:
    def __init__(self,val):
        self.val=val
        self.next=None


class stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return not self.top

    def push(self,val):
        new_node = Node(val)
        if self.is_empty():
            self.top=new_node
        else:
            new_node.next=self.top
            self.top=None
            self.top=new_node
        return

    def pop(self):
        if self.is_empty():
            print('Stack is empty!!')
            return
        else:
            val=self.top.val
            self.top=self.top.next
            return val

    def peek(self):
        if self.is_empty():
            print('Stack is empty!!')
            return
        return self.top.val

    def print_stack(self):
        tmp=self.top
        print('---------stack---------')
        while tmp:
            print(tmp.val)
            tmp=tmp.next
        print('-----------------------')


if __name__ == '__main__':
    stk = stack()
    print(stk.is_empty())

    stk.push(10)
    stk.push(101)
    stk.push(98)
    stk.push(20)
    stk.push(36)
    stk.push(15)

    stk.print_stack()
    print('stk peek ele = ',stk.peek())
    print('popping---------------')
    print(stk.pop())
    print(stk.pop())
    print(stk.pop())
    print('\nAfter popping =>\nstk peek ele = ', stk.peek())
    stk.print_stack()