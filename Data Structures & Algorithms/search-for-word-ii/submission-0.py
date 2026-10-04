from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}

        for word in words:
            node = trie
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node["$"] = word

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, parent):
            char = board[r][c]
            if char not in parent:
                return

            node = parent[char]
            word = node.pop("$", None)
            if word is not None:
                result.append(word)

            board[r][c] = "#"  # Prevent reusing this cell

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if board[nr][nc] in node:
                        dfs(nr, nc, node)

            board[r][c] = char

            # Remove branches with no remaining words
            if not node:
                del parent[char]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie)

        return result