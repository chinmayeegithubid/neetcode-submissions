class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        answer = [0] * len(heights)
        stack = []

        for i in range(len(heights) - 1, -1, -1):
            while stack and stack[-1] < heights[i]:
                stack.pop()
                answer[i] += 1

            if stack:
                answer[i] += 1

            stack.append(heights[i])

        return answer