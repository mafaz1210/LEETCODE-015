class Solution:
    def findDifferentBinaryString(self, nums):
        result = []
        for i, s in enumerate(nums):
            result.append('1' if s[i] == '0' else '0')
        return ''.join(result)
        