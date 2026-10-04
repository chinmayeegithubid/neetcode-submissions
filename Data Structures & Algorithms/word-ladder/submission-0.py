from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        patterns = defaultdict(list)
        length = len(beginWord)

        for word in wordList:
            for i in range(length):
                pattern = word[:i] + "*" + word[i + 1:]
                patterns[pattern].append(word)

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            word, steps = queue.popleft()

            if word == endWord:
                return steps

            for i in range(length):
                pattern = word[:i] + "*" + word[i + 1:]

                for neighbor in patterns.pop(pattern, []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, steps + 1))

        return 0