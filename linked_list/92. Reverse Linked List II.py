# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        '''
        Linked list problem
        '''

        # Edge case: if left == right, no need to reverse anything
        if left == right:
            return head
        
        # Step 1: Store node references in a dictionary
        dictToclass = {}
        curr = head
        count = 1
        
        while curr:
            dictToclass[count] = curr
            curr = curr.next
            count += 1
        
        # Step 2: Reverse values between left and right
        while left < right:
            dictToclass[left].val, dictToclass[right].val = dictToclass[right].val, dictToclass[left].val
            left += 1
            right -= 1
        
        # Step 3: Reconstruct the linked list from the modified dictionary
        new_head = dictToclass[1]
        curr = new_head
        for i in range(2, count):
            curr.next = dictToclass[i]
            curr = curr.next
        curr.next = None
        
        return new_head
