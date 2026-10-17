from functools import cache


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @cache
        def compute(start, end):
            results = []

            for i in range(start, end):
                operator = expression[i]

                if operator not in "+-*":
                    continue

                left_results = compute(start, i)
                right_results = compute(i + 1, end)

                for left in left_results:
                    for right in right_results:
                        if operator == "+":
                            results.append(left + right)
                        elif operator == "-":
                            results.append(left - right)
                        else:
                            results.append(left * right)

            return results or [int(expression[start:end])]

        return compute(0, len(expression))