# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        '''
        Linked list problem -- rotate the list by k times
        '''
        if not head or k == 0:
            return head
        
        # Step 1: Calculate the length of the linked list
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1
        
        # Step 2: Normalize k
        k = k % length
        #print("k value",k)
        if k == 0:
            return head
        
        # Step 3: Find the new tail and new head
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        
        # Step 4: Perform the rotation
        new_tail.next = None
        current.next = head  # Connect the old tail to the old head
        
        return new_head




        