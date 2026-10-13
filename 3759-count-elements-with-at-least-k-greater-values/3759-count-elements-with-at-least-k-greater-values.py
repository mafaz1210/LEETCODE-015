from bisect import bisect_right

class Solution:
    def countElements(self, nums, k):
        n = len(nums)
        sorted_nums = sorted(nums)
        count = 0
        
        for x in nums:
            greater_count = n - bisect_right(sorted_nums, x)
            if greater_count >= k:
                count += 1
        
        return count