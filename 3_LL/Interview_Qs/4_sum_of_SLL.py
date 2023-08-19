import time
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


def add_sll(num1,num2):
    ans_node=Node(0)
    ans=ans_node
    carry_fw=0
    while num1 or num2:
        if num1 and num2:
            print(f'num1 data = {num1.data}, num2 data = {num2.data}, carry_fw = {carry_fw}')
            digit_ans=(num1.data+num2.data)+carry_fw
            num1 = num1.next
            num2 = num2.next
        elif num1:
            digit_ans = num1.data+carry_fw
            print(f'num1 data = {num1.data}, carry_fw = {carry_fw}')
            num1 = num1.next
        elif num2:
            digit_ans = num2.data+carry_fw
            print(f'num2 data = {num2.data}, carry_fw = {carry_fw}')
            num2 = num2.next
        carry_fw=digit_ans//10

        ans_node.next=Node(digit_ans%10)
        ans_node=ans_node.next

    if carry_fw in range(1,10):
        ans_node.next = Node(carry_fw)


    return ans.next

def print_sll(start:Node):
    while start:
        print(str(start.data)+',',end='')
        start=start.next
    print()

if __name__ == '__main__':
    # num1=Node(0)
    # num1.next=Node(9)
    # num1.next.next=Node(9)
    # num1.next.next.next=Node(9)
    # num1.next.next.next.next=Node(9)
    # num1.next.next.next.next.next=Node(9)
    # num1.next.next.next.next.next.next=Node(9)
    #
    #
    # num2=Node(1)
    # num2.next=Node(9)
    # num2.next.next=Node(9)
    # num2.next.next.next=Node(9)
    #
    # ans=add_sll(num1,num2)
    # print('------------------------------')
    # print_sll(ans)
#
#
    num1=Node(2)
    num1.next=Node(4)
    num1.next.next=Node(3)



    num2=Node(5)
    num2.next=Node(6)
    num2.next.next=Node(4)

    ans=add_sll(num1,num2)
    print('------------------------------')
    print_sll(ans)
