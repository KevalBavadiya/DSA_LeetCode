class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        freq = 0
        left = 0
        total = 0
        right = 0
        while right < len(nums):
            total += nums[right]
            while nums[right]*(right-left+1)- total > k:
                total -= nums[left]
                left += 1
            freq = max(freq, right-left+1)
            right += 1
        return freq