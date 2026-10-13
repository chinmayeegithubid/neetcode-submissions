class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n

        balls = moves = 0
        for i in range(n):
            answer[i] += moves
            balls += boxes[i] == "1"
            moves += balls

        balls = moves = 0
        for i in range(n - 1, -1, -1):
            answer[i] += moves
            balls += boxes[i] == "1"
            moves += balls

        return answer