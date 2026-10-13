class Solution {
public:
    int findComplement(int num) {
        // Step 1: Find number of bits in num
        int mask = 0;
        int temp = num;
        
        while (temp > 0) {
            mask = (mask << 1) | 1; // build mask like 111...
            temp >>= 1;
        }
        
        // Step 2: XOR with mask to flip bits
        return num ^ mask;
    }
};
