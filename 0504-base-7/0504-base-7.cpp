class Solution {
public:
    string convertToBase7(int num) {
        if (num == 0) return "0"; // Special case
        
        bool isNegative = num < 0;
        num = abs(num);
        
        string result = "";
        
        while (num > 0) {
            result = to_string(num % 7) + result; // prepend remainder
            num /= 7;
        }
        
        if (isNegative) result = "-" + result;
        
        return result;
    }
};
