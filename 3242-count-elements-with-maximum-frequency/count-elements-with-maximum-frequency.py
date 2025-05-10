class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        temp = {}
        for i in range(len(nums)):
            if nums[i] in temp: 
                temp[nums[i]] += 1
            else:
                temp[nums[i]] = 1
        max_freq, count = 0,0
        for i in temp:
            if max_freq<temp[i]:
                max_freq = temp[i]
        for i in temp:
            if temp[i]== max_freq:
                count+=temp[i]
        return count     
        #print(temp)
        