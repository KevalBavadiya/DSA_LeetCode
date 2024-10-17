class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for i, num in enumerate(nums):
            if target-num in sums:
                return([sums[target-num],i])
            elif num not in sums:
                sums[num] = i