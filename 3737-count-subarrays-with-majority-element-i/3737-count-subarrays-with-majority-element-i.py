class Solution:
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)
        count = 0
        
        for start in range(n):
            running_sum = 0
            for end in range(start, n):
                running_sum += 1 if nums[end] == target else -1
                if running_sum > 0:
                    count += 1
        
        return count