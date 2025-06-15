class Solution:
    def merge(self, nums, low, mid, high):
        temp = []
        left = low
        right = mid+1
        while left<= mid and right<=high:
            if nums[left]<=nums[right]:
                temp.append(nums[left])
                left += 1
            else :
                temp.append(nums[right])
                right += 1
        while left<=mid:
            temp.append(nums[left])
            left += 1
        
        while right<=high:
            temp.append(nums[right])
            right += 1
        for i in range(len(temp)):
            nums[low+i]= temp[i]

    def merge_sort(self,nums,low, high):
        if low>=high :
            return
        mid = int((low + high)/2)
        #print(mid)
        self.merge_sort(nums, low, mid)
        self.merge_sort(nums, mid+1, high)
        self.merge(nums, low, mid, high)

    def sortArray(self, nums: List[int]) -> List[int]:
        low = 0
        high = len(nums)-1
        self.merge_sort(nums,low, high)
        return nums