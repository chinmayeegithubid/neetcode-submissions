from collections import Counter


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = Counter(arr)

        for word in arr:
            if counts[word] == 1:
                k -= 1
                if k == 0:
                    return word

        return ""