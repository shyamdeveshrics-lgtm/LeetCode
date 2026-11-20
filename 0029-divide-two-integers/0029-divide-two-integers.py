
class Solution(object):
    def divide(self, dividend, divisor):
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        sign = -1 if (dividend < 0) != (divisor < 0) else 1

        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0

        while dividend >= divisor:
            temp = divisor
            count = 1

            while dividend >= (temp << 1):
                temp = temp << 1
                count = count << 1

            dividend -= temp
            result += count

        if sign < 0:
            return -result
        return result
