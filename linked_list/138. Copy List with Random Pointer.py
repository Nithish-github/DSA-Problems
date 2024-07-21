"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        '''
        Needed to create a deep copy of the linked list
        Think in the way of using dict 
        '''
        dicttoclass = {None:None}

        curr = head

        #Single pass to copy all the nodes
        while curr:
            dicttoclass[curr] = Node(curr.val)
            curr = curr.next


        #second pass to create the deep copy
        #make again cur to head
        curr = head
        while curr:
            copy = dicttoclass[curr]
            copy.next = dicttoclass[curr.next]
            copy.random = dicttoclass[curr.random]

            curr = curr.next


        return dicttoclass[head]

