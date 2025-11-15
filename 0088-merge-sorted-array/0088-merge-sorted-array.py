class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        [1,2,3, 0, 0, 0] m = 3
        [2, 5, 6] n = 3

        nums1[n1] = 3
        nums2[n2] = 6
        """
        
        n1, n2, nT = m-1, n - 1, m + n - 1
        while n1 >= 0 and n2 >= 0: 
            if nums1[n1] < nums2[n2]:
                nums1[nT] = nums2[n2]
                n2 -= 1
            else: 
                nums1[nT] = nums1[n1]
                n1 -= 1
            nT -= 1
        print(n1, n2, nT, nums1, nums2)
        if n2 >= 0: nums1[:nT+1] = nums2[:n2+1]
        
            

            
