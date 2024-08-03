# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        '''
        Linked problem --- Neetcode idea is to create two list like left and right list 
        '''
        left  , right = ListNode() , ListNode()
        ltail , rtail = left , right

        while head:
            if head.val < x:
                ltail.next = head
                ltail  = ltail.next

            else:
                rtail.next = heads
                rtail = rtail.next

            head = head.next

        ltail.next = right.next
        rtail.next = None

        return left.next


        