class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k%=len(nums)
        nums.reverse()
        #print(nums)
        nums[:k]=reversed(nums[:k])
        #[::-1]+
        nums[k:]=reversed(nums[k:])
        #[::-1]
        #print(nums[:k].reverse())
        
        