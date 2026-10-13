class Solution:
    def remapDigit(self, x: int, fro: int, to: int) -> int:
        if fro == to: return x
        answer = x
        rem = x
        p = 1
        while rem > 0:
            if rem % 10 == fro:
                answer += (to - fro) * p
            p *= 10
            rem //= 10
        return answer

    def minMaxDifference(self, num: int) -> int:
        k = 9 # First digit.
        m = 0 # First digit below nine.
        rem = num
        while rem > 0:
            digit = rem % 10
            k = digit
            if digit != 9:
                m = digit
            rem //= 10
        return self.remapDigit(num, m, 9) - self.remapDigit(num, k, 0)