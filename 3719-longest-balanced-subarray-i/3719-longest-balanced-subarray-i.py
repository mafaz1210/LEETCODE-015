class Solution:
    def longestBalanced(self, nums):
        n = len(nums)
        max_len = 0
        
        for start in range(n):
            evens = set()
            odds = set()
            for end in range(start, n):
                if nums[end] % 2 == 0:
                    evens.add(nums[end])
                else:
                    odds.add(nums[end])
                
                if len(evens) == len(odds) and len(evens) > 0:
                    max_len = max(max_len, end - start + 1)
        
        return max_len