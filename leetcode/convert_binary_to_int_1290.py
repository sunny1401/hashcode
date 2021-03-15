# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0
# or 1. The linked list holds the binary representation of a number.
#
# Return the decimal value of the number in the linked list.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getDecimalValue(self, head: ListNode) -> int:
    temp = head
    l_size = 0
    while (temp):
        l_size += 1
        temp = temp.next

    print(l_size)

    int_num = 0
    while (head):
        int_num += (head.val * pow(2, l_size - 1))
        l_size -= 1
        head = head.next

    return int_num
