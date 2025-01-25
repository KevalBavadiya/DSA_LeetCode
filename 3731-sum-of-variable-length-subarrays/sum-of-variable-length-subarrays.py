class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        sum = [0]* len(nums)
        ans = 0
        #max_idx = 0
        for i in range(len(nums)):
            sum[i] = sum[i-1]+nums[i]
        print(sum)
        for i in range(len(nums)):
            max_idx = max(0, i- nums[i])
            ans += sum[i]
            if max_idx >= 1: 
                ans -=sum[max_idx -1]
        return ans





        