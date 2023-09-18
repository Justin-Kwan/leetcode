// custom integer type that stores int in log form to avoid integer
// overflow when multiplying large integers
class Integer {
private:
    int sign;
    double value;

    Integer(int sign, double value) : sign{sign}, value{value} {
    }

public:
    Integer(int number) {
        if (number == 0) {
            this->sign = 0;
            this->value = 0;
        }
        else {
            this->sign = number < 0 ? -1 : 1;
            this->value = log(abs(number));
        }
    }

    bool operator < (const Integer &other) const {
        if(this->sign != other.sign) {
            return this->sign < other.sign;
        }
        // both integers have same sign so compare them differently
        // depending on whether they are negative or positive
        if (this->sign < 0) {
            return this->value > other.value;
        }
        else {
            return this->value < other.value;
        }
    }

    Integer operator * (const Integer &other) const {
        // product is zero if either Integer is zero
        if (!this->sign || !other.sign) {
            return Integer(0, 0);
        }
        // log rule states that log(x * y) = log(x) + log(y)
        return Integer(this->sign * other.sign, this->value + other.value);
    }

    int integer() const {
        if (this->sign == 0) {
            return 0;
        }
        // e raised to power of log value obtains original argument
        return this->sign * (int)round(exp(this->value));
    }
};

class Solution {
public:
    // bottom up dp approach
    int maxProduct(vector<int> &nums) {
        if (nums.empty()) {
            return 0;
        }

        Integer maxProduct = Integer(nums[0]);
        Integer curMaxProduct = Integer(1);
        Integer curMinProduct = Integer(1);

        for (int i = 0; i < nums.size(); ++i) {
            Integer num = Integer(nums[i]);
            // negative number should consider itself multiplied against
            // minimum subarray product up to previous to obtain max product
            // up to itself (since negative * negative > negative * position)
            if (num < Integer(0)) {
                swap(curMaxProduct, curMinProduct);
            }

            curMaxProduct = max(curMaxProduct * num, num);
            curMinProduct = min(curMinProduct * num, num);
            maxProduct = max(maxProduct, curMaxProduct);
        }

        return maxProduct.integer();
    }
};
