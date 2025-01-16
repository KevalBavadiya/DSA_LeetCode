class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        temp = {}
        for i, n in enumerate(nums):
            if n in temp and abs(temp[n]-i)<=k :
                return True
            temp[n]=i
        return False