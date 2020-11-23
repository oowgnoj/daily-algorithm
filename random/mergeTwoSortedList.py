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
        ans = new ListNode()
        while l1.next == None and l2.next == None:
        	if l1.val >= l2.val:
        		ans.val = l1.val
        		l1 = l1.next
    		else:
    			ans.val = l2.val
    			l2 = l2.next
		return ans