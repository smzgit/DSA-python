'''
Question: Design a Data Structure SpecialStack that supports all the stack operations like
           push(), pop(), isEmpty(), isFull() and an additional operation getMin() which should
           return minimum element from the SpecialStack.
           All these operations of SpecialStack must be O(1).
'''
from collections import deque
class Special_Stack:
    def __init__(self):
        self.stk=deque()
        self.min_stk=deque()

    def push_mini(self,ele):
        if len(self.min_stk)==0:
            self.min_stk.append(ele)
        else:
            if ele<self.min_stk[-1]:
                self.min_stk.append(ele)

    def pop_mini(self,ele):
        if ele==self.min_stk[-1]:
            self.min_stk.pop()

    def push(self,ele):
        self.stk.append(ele)
        self.push_mini(ele)

    def pop(self):
        if len(self.min_stk) == 0:
            print('stack is empty')
            return
        else:
            val=self.stk.pop()
            self.pop_mini(val)
            return val

    def peek(self):
        if len(self.stk) == 0:
            print('stack is empty')
            return
        else:
            return self.stk[-1]

    def get_min(self):
        if len(self.min_stk) == 0:
            print('stack is empty')
            return
        else:
            return self.min_stk[-1]

    def __str__(self):
        val=[str(x) for x in self.stk]
        return '['+' ['.join(val)


if __name__ == '__main__':
    stk=Special_Stack()
    stk.push(12)
    stk.push(3)
    stk.push(20)
    print(stk)
    print('mini ele in stack = ',stk.get_min())
    stk.push(1)
    stk.push(2)
    print(stk)
    print('mini ele in stack = ',stk.get_min())
    stk.pop()
    print(stk)
    print('mini ele in stack = ',stk.get_min())

