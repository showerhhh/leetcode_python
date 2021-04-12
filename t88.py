class Solution:
    def merge(self, nums1, m: int, nums2, n: int):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums = []
        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        while i < m:
            nums.append(nums1[i])
            i += 1
        while j < n:
            nums.append(nums2[j])
            j += 1

        for i in range(m + n):
            nums1[i] = nums[i]
