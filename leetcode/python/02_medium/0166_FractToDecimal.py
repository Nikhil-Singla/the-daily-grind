# [A1] [S.CHECK] [M.CHECK] [EDT]

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
        ongoing_decimal = []

        while remainder != 0:
            if remainder in remainders:
                repition_temp = remainders[remainder]
                ongoing_decimal.insert(repition_temp, "(")
                ongoing_decimal.append(")")
                break

            remainders[remainder] = len(ongoing_decimal)
            remainder *= 10
            digit = remainder // denominator

            ongoing_decimal.append(str(digit))
            remainder %= denominator

        return result + "".join(ongoing_decimal)