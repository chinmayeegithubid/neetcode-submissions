class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        top_remaining = sum(grid[0])
        bottom_previous = 0
        answer = top_remaining

        for col in range(len(grid[0])):
            top_remaining -= grid[0][col]

            second_score = max(top_remaining, bottom_previous)
            answer = min(answer, second_score)

            bottom_previous += grid[1][col]

        return answer