from collections import deque

class Queue:
    def __init__(self):
        self.q = deque()

    def is_empty(self):
        return len(self.q)==0

    def enque(self,data):
        self.q.append(data)

    def deque(self):
        if self.is_empty():
            print('Queue is empty')
            return
        return self.q.popleft()

    def peek(self):
        if self.is_empty():
            print('Queue is empty')
            return
        return self.q[0]
    def del_que(self):
        self.q.clear()
        print('whole queue deleted !!')
        return

    def __str__(self):
        print('\nQueue--------------->')
        v=[str(x) for x in self.q]
        return '[F] '+' - '.join(v)+' [R]'


if __name__ == '__main__':
    my_q = Queue()
    print('is q empty??\nans -> ',my_q.is_empty())
    my_q.enque(12)
    my_q.enque(51)
    my_q.enque(89)
    my_q.enque(100)
    print(my_q)

    my_q.deque()
    print(my_q)
    my_q.deque()
    print(my_q)
    my_q.enque(2131)
    my_q.enque(931)
    my_q.enque(31)
    my_q.enque(211)
    print(my_q)
    print('\nPeek element = ',my_q.peek())

    my_q.del_que()
    print(my_q)


