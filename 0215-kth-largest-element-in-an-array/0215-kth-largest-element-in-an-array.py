import random

class Solution:
    def findKthLargest(self, nums, k):
        target_idx = len(nums) - k  # index of kth largest in ascending sorted order
        
        left, right = 0, len(nums) - 1
        while left < right:
            pivot_val = nums[random.randint(left, right)]
            
            lt, gt = left, right
            i = left
            while i <= gt:
                if nums[i] < pivot_val:
                    nums[i], nums[lt] = nums[lt], nums[i]
                    lt += 1
                    i += 1
                elif nums[i] > pivot_val:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                    # don't advance i here — need to check swapped-in value
                else:
                    i += 1
            
            # After this, nums[lt..gt] are all == pivot_val
            if target_idx < lt:
                right = lt - 1
            elif target_idx > gt:
                left = gt + 1
            else:
                return pivot_val  # target_idx falls within the equal-to-pivot band
        
        return nums[left]
        