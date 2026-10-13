#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        // dp[i][j] = max number of strings using at most i zeros and j ones
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        
        for (const string &s : strs) {
            int zeros = 0, ones = 0;
            for (char c : s) {
                if (c == '0') ++zeros;
                else ++ones;
            }
            // reverse iterate to avoid using the same string multiple times
            for (int i = m; i >= zeros; --i) {
                for (int j = n; j >= ones; --j) {
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1);
                }
            }
        }
        return dp[m][n];
    }
};

// Example usage (uncomment to test locally)
// int main() {
//     Solution sol;
//     vector<string> strs = {"10","0001","111001","1","0"};
//     cout << sol.findMaxForm(strs, 5, 3) << "\n"; // expected 4
// }
