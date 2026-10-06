# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        lengthList = 0
        curr = head
        # Find len of list
        while curr:
            lengthList += 1
            curr = curr.next

        # len-n -> that is what we are removing
        removedIndex = lengthList - n
        
        if removedIndex == 0:
            return head.next
        
        curr = head

        for i in range(lengthList - 1):
            if (i + 1) == removedIndex:
                curr.next = curr.next.next
                break
            curr = curr.next

        return head

        