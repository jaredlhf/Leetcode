# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertToBST(self, start, end):
        if start == end:
            return None

        fast = slow = start
        while fast != end and fast.next != end:
            fast = fast.next.next
            slow = slow.next
        
        head = TreeNode(slow.val)
        
        head.left = self.convertToBST(start, slow)
        head.right = self.convertToBST(slow.next, end)
        return head

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        return self.convertToBST(head, None)
        
        
