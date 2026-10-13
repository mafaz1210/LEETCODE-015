class Solution:
    def findMissingElements(self, nums):
        full_range = set(range(min(nums), max(nums) + 1))
        return sorted(full_range - set(nums))