# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        start = 0
        end = len(nums)-1
        if start > end :
            return None
        mid = (end-start)//2
        return TreeNode(nums[mid], self.sortedArrayToBST(nums[:mid]), self.sortedArrayToBST(nums[mid+1:]))