class Solution {
public:
    int sumBase(int n, int k) {
        int sum = 0;
        while (n > 0) {
            sum += n % k;   // add remainder (digit in base k)
            n /= k;         // move to next digit
        }
        return sum;
    }
};
