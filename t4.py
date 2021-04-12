class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        m = len(nums1)
        n = len(nums2)
        i = 0
        j = 0
        k = 0

        def check(k):
            if k == (m + n) // 2:
                return True
            elif (m + n) % 2 == 0 and k == (m + n) // 2 - 1:
                return True
            else:
                return False

        count = []
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                if check(k):
                    count.append(nums1[i])
                k += 1
                i += 1
            else:
                if check(k):
                    count.append(nums2[j])
                k += 1
                j += 1
        while i < m:
            if check(k):
                count.append(nums1[i])
            k += 1
            i += 1
        while j < n:
            if check(k):
                count.append(nums2[j])
            k += 1
            j += 1
        return sum(count) / len(count)
