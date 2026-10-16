from collections import Counter


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        counts = Counter()
        multipliers = []
        multiplier = 1
        count = 1
        i = len(formula) - 1

        while i >= 0:
            char = formula[i]

            if char.isdigit():
                end = i
                while i >= 0 and formula[i].isdigit():
                    i -= 1
                count = int(formula[i + 1:end + 1])

            elif char == ")":
                multipliers.append(count)
                multiplier *= count
                count = 1
                i -= 1

            elif char == "(":
                multiplier //= multipliers.pop()
                i -= 1

            else:
                end = i
                while i >= 0 and formula[i].islower():
                    i -= 1

                element = formula[i:end + 1]
                counts[element] += count * multiplier
                count = 1
                i -= 1

        return "".join(
            element + (str(counts[element]) if counts[element] > 1 else "")
            for element in sorted(counts)
        )