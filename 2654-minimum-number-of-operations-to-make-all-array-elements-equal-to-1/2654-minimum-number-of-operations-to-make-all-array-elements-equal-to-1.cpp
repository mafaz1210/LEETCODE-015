#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n = nums.size();
        int g = nums[0];
        
        // Step 1: Find GCD of all elements
        for (int i = 1; i < n; ++i)
            g = gcd(g, nums[i]);
        
        // If overall GCD > 1, impossible
        if (g != 1)
            return -1;
        
        // Step 2: Count ones
        int ones = count(nums.begin(), nums.end(), 1);
        if (ones > 0)
            return n - ones;
        
        // Step 3: Find minimum length subarray with GCD == 1
        int minLen = n + 1;
        for (int i = 0; i < n; ++i) {
            int currGCD = nums[i];
            for (int j = i; j < n; ++j) {
                currGCD = gcd(currGCD, nums[j]);
                if (currGCD == 1) {
                    minLen = min(minLen, j - i + 1);
                    break;
                }
            }
        }

        // Total operations: (minLen - 1) + (n - 1)
        return (minLen - 1) + (n - 1);
    }
};
