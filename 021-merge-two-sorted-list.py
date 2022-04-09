# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# don't understand linked lists wth
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> ListNode:
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next

        tail = tail.next

    while list1:
        tail.next = list1
        list1 = list1.next

    while list2:
        tail.next = list2
        list2 = list2.next

    return dummy.next


print(mergeTwoLists(
    [1, 2, 4],
    [1, 3, 4]))
