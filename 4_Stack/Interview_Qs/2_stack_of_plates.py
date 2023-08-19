'''
Stack of Plates:
Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold.
Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks
and should create a new stack once the previous one exceeds capacity.

SetOfStacks.push () and SetOfStacks.pop() should behave identically to a single stack, that is,
pop () should return the same values as it would if there were just a single stack.
FOLLOW UP
Implement a function popAt (int index) which performs a pop operation on a specific substack.
'''


class StackOfPlates:
    def __init__(self,size):
        self.row_limit=size
        self.set_of_stacks = [ [ -1 for i in range(size) ] for j in range(self.row_limit) ]
        self.ind = 0
        self.stack_row=0
        self.size=size

    def add_row(self):
        self.set_of_stacks.append([ -1 for i in range(self.size) ])
        self.row_limit+=1

    def push(self,ele):
        if self.ind>=self.size:
            self.stack_row+=1
            self.ind=self.ind%self.size
        if self.stack_row>=self.row_limit:
            self.add_row()

        self.set_of_stacks[self.stack_row][self.ind]=ele
        self.ind+=1

    def pop(self):
        self.ind-=1
        if len(self.set_of_stacks)==0:
            print('set of plates is empty!!')
            return
        val=self.set_of_stacks[self.stack_row][self.ind]
        print('popped out = ',val)
        self.set_of_stacks[self.stack_row][self.ind]=-1
        if self.ind==0:
            self.stack_row-=1
            self.ind=self.size
            self.set_of_stacks.pop()
            self.row_limit-=1
        return val
    def pop_at(self,i):
        self.ind-=1
        if len(self.set_of_stacks)==0:
            print('set of plates is empty!!')
            return
        if self.set_of_stacks[i][-1]==-1:
            print('no val available !!')
            return
        val=self.set_of_stacks[i].pop(-1)
        return val


    def print_sop(self):
        for i in self.set_of_stacks:
            print(i)




if __name__ == '__main__':
    sop = StackOfPlates(5)
    sop.push(1)
    sop.push(2)
    sop.push(3)
    sop.push(4)
    sop.push(5)
    sop.push(6)
    sop.push(7)
    sop.push(11)
    sop.push(12)
    sop.push(13)
    sop.push(14)
    sop.push(15)
    sop.push(16)
    sop.push(17)

    sop.push(101)
    sop.push(102)
    sop.push(103)
    sop.push(104)
    sop.push(105)
    sop.push(106)
    sop.push(107)

    sop.push(54)
    sop.push(505)
    sop.push(506)
    sop.push(507)
    sop.push(1507)
    sop.push(2507)
    sop.push(3507)
    sop.push(4507)
    sop.push(9907)
    sop.push(8507)
    sop.push(47)
    sop.push(97)
    sop.push(687)
    sop.push(687)
    sop.push(687)

    sop.push(1007)
    sop.push(1009)
    sop.push(1001)
    sop.push(1100)
    sop.push(21100)

    sop.print_sop()

    print('popping---------------->')
    sop.pop()
    sop.pop()
    sop.pop()
    sop.pop()
    sop.pop()
    sop.pop()
    sop.pop()
    sop.pop()
    sop.pop()



    sop.print_sop()

    print(sop.pop_at(3))
    sop.print_sop()



