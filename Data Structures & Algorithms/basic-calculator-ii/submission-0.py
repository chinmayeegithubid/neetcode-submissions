class Solution:
    def calculate(self, s: str) -> int:
        total = 0
        last = 0
        number = 0
        operator = "+"

        for i, char in enumerate(s):
            if "0" <= char <= "9":
                number = number * 10 + ord(char) - ord("0")

            if char in "+-*/" or i == len(s) - 1:
                if operator == "+":
                    total += last
                    last = number
                elif operator == "-":
                    total += last
                    last = -number
                elif operator == "*":
                    last *= number
                else:
                    last = (
                        last // number
                        if last >= 0
                        else -((-last) // number)
                    )

                operator = char
                number = 0

        return total + last