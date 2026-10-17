class Solution:
    def maxLength(self, arr: List[str]) -> int:
        masks = []

        for word in arr:
            mask = 0

            for char in word:
                bit = 1 << (ord(char) - ord("a"))
                if mask & bit:
                    break
                mask |= bit
            else:
                masks.append(mask)

        def backtrack(index, used):
            if index == len(masks):
                return used.bit_count()

            best = backtrack(index + 1, used)

            if not used & masks[index]:
                best = max(
                    best,
                    backtrack(index + 1, used | masks[index])
                )

            return best

        return backtrack(0, 0)