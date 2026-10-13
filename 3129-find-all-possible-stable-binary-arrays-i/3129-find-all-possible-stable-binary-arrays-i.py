class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        dp0 = [[0] * (one + 1) for _ in range(zero + 1)]
        dp1 = [[0] * (one + 1) for _ in range(zero + 1)]
        
        # Base cases: all zeros / all ones
        for i in range(1, min(zero, limit) + 1):
            dp0[i][0] = 1
        for j in range(1, min(one, limit) + 1):
            dp1[0][j] = 1
        
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                # end with a run of k zeros, k from 1..min(limit, i)
                s0 = 0
                for k in range(1, min(limit, i) + 1):
                    s0 += dp1[i - k][j]
                dp0[i][j] = s0 % MOD
                
                # end with a run of k ones, k from 1..min(limit, j)
                s1 = 0
                for k in range(1, min(limit, j) + 1):
                    s1 += dp0[i][j - k]
                dp1[i][j] = s1 % MOD
        
        return (dp0[zero][one] + dp1[zero][one]) % MOD