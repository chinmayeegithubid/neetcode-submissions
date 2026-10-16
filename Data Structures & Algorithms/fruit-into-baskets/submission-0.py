class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counts = {}
        left = 0
        result = 0

        for right, fruit in enumerate(fruits):
            counts[fruit] = counts.get(fruit, 0) + 1

            while len(counts) > 2:
                outgoing = fruits[left]
                counts[outgoing] -= 1

                if counts[outgoing] == 0:
                    del counts[outgoing]

                left += 1

            result = max(result, right - left + 1)

        return result