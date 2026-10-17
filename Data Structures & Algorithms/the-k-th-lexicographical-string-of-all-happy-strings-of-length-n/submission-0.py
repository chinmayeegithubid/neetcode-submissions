class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k > 3 * (1 << (n - 1)):
            return ""

        result = []

        for i in range(n):
            block_size = 1 << (n - i - 1)

            for char in "abc":
                if result and char == result[-1]:
                    continue

                if k > block_size:
                    k -= block_size
                else:
                    result.append(char)
                    break

        return "".join(result)