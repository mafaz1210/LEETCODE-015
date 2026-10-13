class Solution {
public:
    string addBinary(string a, string b) {
        string result = "";
        int i = a.size() - 1;
        int j = b.size() - 1;
        int carry = 0;

        while (i >= 0 || j >= 0 || carry) {
            int sum = carry;
            if (i >= 0) sum += a[i--] - '0';  // convert char to int
            if (j >= 0) sum += b[j--] - '0';  // convert char to int
            result += (sum % 2) + '0';        // append current bit
            carry = sum / 2;                  // calculate new carry
        }

        reverse(result.begin(), result.end()); // reverse the result string
        return result;
    }
};
