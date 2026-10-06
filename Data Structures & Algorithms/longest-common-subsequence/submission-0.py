class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Keep the DP array sized to the shorter string.
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        dp = [0] * (len(text2) + 1)

        for char1 in text1:
            diagonal = 0

            for j, char2 in enumerate(text2, start=1):
                above = dp[j]

                if char1 == char2:
                    dp[j] = diagonal + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])

                diagonal = above

        return dp[-1]