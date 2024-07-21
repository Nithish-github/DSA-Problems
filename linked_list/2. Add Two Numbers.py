# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        '''
        Linked List Problem
        '''

        dummy  = ListNode()
        cur = dummy 
        carry = 0

        while l1 or l2 or carry:

            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0

            value = value1 + value2 + carry

            carry = value // 10
            value_to_append = value % 10

            #update the current value to the linked list
            cur.next = ListNode(value_to_append)

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None


        return dummy.next

        