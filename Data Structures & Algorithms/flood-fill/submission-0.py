class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]

        if original == color:
            return image

        rows, cols = len(image), len(image[0])
        stack = [(sr, sc)]
        image[sr][sc] = color

        while stack:
            row, col = stack.pop()

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                r, c = row + dr, col + dc

                if 0 <= r < rows and 0 <= c < cols and image[r][c] == original:
                    image[r][c] = color
                    stack.append((r, c))

        return image