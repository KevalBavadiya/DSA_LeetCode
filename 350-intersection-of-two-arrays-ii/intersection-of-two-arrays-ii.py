class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = len(nums1)
        n2 = len(nums2)
        res = []
        if n1 > n2 : 
            for i in  nums1:
                if i in nums2:
                    res.append(i)
                    nums2.remove(i)
        else :
            for i in nums2:
                if i in nums1:
                    res.append(i)
                    nums1.remove(i)
        return res