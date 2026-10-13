class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:

        return sum(nlargest(2,nums)) - min(nums)
 