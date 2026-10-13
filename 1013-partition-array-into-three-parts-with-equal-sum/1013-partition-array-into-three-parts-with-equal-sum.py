class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3 == 0:
            total = total // 3
        curr = 0
        ans = 0
        for num in arr:
            curr += num
            if curr == total:
                ans += 1
                curr = 0
            if ans == 3:
                return True
        return False