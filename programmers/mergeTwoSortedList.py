# Runtime: 20 ms, faster than 92.68% of Python online submissions for Merge Two Sorted Lists.
# Memory Usage: 13.4 MB, less than 85.13% of Python online submissions for Merge Two Sorted Lists.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return l1
        
        ans = ListNode()
        tail = ans
        while True:
            if l1 and l2:
                if l1.val >= l2.val:
                    tail.val = l2.val
                    l2= l2.next
                else:
                    tail.val = l1.val
                    l1= l1.next
                    
            else:
                if l1:
                    tail.val = l1.val
                    l1 = l1.next
                if l2:
                    tail.val = l2.val
                    l2= l2.next
            if l1 == None and l2 == None:
                break
            else:
                tail.next= ListNode()
                tail = tail.next

        return ans