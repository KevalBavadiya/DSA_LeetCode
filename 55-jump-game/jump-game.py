class Solution:
    def canJump(self, nums: List[int]) -> bool:
        targetidx = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if targetidx <= i+nums[i]:
                targetidx = i
                #print(targetidx)
        if targetidx == 0: return True
        else: return False