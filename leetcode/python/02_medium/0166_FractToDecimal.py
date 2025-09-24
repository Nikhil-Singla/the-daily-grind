# [A2] [IMP] [MO] [SO]

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)

        final_sign = (numerator < 0) ^ (denominator < 0)  # Bitwise XOR
        numerator, denominator = abs(numerator), abs(denominator)

        result = "-" if final_sign else ""
        result += str(numerator//denominator) + "."

        remainder = numerator % denominator
        remainders = {}
        ongoing_decimal, count = [], 0

        while remainder != 0:
            if remainder in remainders:
                repition_temp = remainders[remainder]
                ongoing_decimal.insert(repition_temp, "(")
                ongoing_decimal.append(")")
                break

            remainders[remainder] = count
            count += 1
            remainder *= 10

            ongoing_decimal.append(str(remainder // denominator))
            remainder %= denominator

        return result + "".join(ongoing_decimal)