class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Store DP values for the shorter string.
        if len(word1) < len(word2):
            word1, word2 = word2, word1

        dp = list(range(len(word2) + 1))

        for i, char1 in enumerate(word1, start=1):
            diagonal = dp[0]
            dp[0] = i

            for j, char2 in enumerate(word2, start=1):
                above = dp[j]

                if char1 == char2:
                    dp[j] = diagonal
                else:
                    dp[j] = 1 + min(
                        dp[j - 1],  # Insert
                        above,      # Delete
                        diagonal    # Replace
                    )

                diagonal = above

        return dp[-1]