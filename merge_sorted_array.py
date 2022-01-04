class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        r1 = m-1
        r2 = n-1
        p = m+n-1
        while r1>=0 and r2>=0:
            if nums1[r1]>nums2[r2]:
                nums1[p] = nums1[r1]
                r1-=1
                p-=1
            else:
                nums1[p] = nums2[r2]
                r2-=1
                p-=1
        if r1<0:                
            while r2>=0:
                nums1[p] = nums2[r2]
                r2-=1
                p-=1
        elif r2<0:
            while r1>=0:
                nums1[p] = nums1[r1]
                r1-=1
                p-=1
        return nums1