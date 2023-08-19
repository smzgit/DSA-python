from collections import deque

class stack:
    def __init__(self):
        self.stk = deque()

    def is_empty(self):
        return len(self.stk)==0

    def push(self,val):
        self.stk.append(val)

    def pop(self):
        if self.is_empty():
            print('Stack is empty!!')
            return
        return self.stk.pop()

    def peek(self):
        if self.is_empty():
            print('Stack is empty!!')
            return
        return self.stk[-1]

    def print_stack(self):
        print(self.stk)
        return

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