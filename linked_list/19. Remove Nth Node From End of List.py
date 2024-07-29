# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        '''
        Typicall linked list problem 
        '''
        dummy = ListNode()
        dummy.next = head
        first = dummy
        second = dummy 

        #move the first pointer to the n+1 pos
        for _ in range(n+1):
            first = first.next

        #to maintain the gap between the first and the second pointer
        #now move the first pointer to the end
        while first is not None:
            first = first.next
            second = second.next

        
        #now from the first the second is at proper n distance
        second.next = second.next.next


        return dummy.next

        

        