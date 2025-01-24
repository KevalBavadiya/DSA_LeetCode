class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums.sort()
        sum = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[sum]:
                #print(nums[sum])
                sum = sum+1
                #print(nums[sum])
                nums[sum] = nums[i]
                #sum += 1
        #print(nums)
        return sum+1
        