class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = sorted(nums)

        n = len(nums)
        mid = (n + 1) // 2

        left = arr[:mid][::-1]
        right = arr[mid:][::-1]

        i = j = 0

        for k in range(n):
            if k % 2 == 0:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1

    def wiggleSort1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums) - 1, 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]