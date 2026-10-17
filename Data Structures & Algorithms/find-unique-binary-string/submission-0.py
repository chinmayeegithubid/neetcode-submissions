class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return "".join(
            "1" if word[i] == "0" else "0"
            for i, word in enumerate(nums)
        )