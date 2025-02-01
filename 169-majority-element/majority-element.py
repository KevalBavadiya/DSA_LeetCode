class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        temp = {}
        for i in nums:
            temp[i] = temp.get(i,0) + 1
        res = max(temp, key=temp.get)
        return res