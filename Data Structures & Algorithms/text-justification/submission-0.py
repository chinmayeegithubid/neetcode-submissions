class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        start = 0
        n = len(words)

        while start < n:
            end = start
            letters = 0

            while (
                end < n
                and letters + len(words[end]) + (end - start) <= maxWidth
            ):
                letters += len(words[end])
                end += 1

            gaps = end - start - 1

            if end == n or gaps == 0:
                line = " ".join(words[start:end])
                line += " " * (maxWidth - len(line))
            else:
                spaces, extra = divmod(maxWidth - letters, gaps)
                parts = []

                for i in range(start, end - 1):
                    parts.append(words[i])
                    padding = spaces + (i - start < extra)
                    parts.append(" " * padding)

                parts.append(words[end - 1])
                line = "".join(parts)

            result.append(line)
            start = end

        return result